
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

class SentimentAnalysis:
    def __init__(self,from_loc,to_loc):
        analyzer = SentimentIntensityAnalyzer()
        self.frompath = from_loc
        self.topath = to_loc

        li_files = os.listdir(self.frompath)
        headers = ['PRODUCT_NAME','PRODUCT_LINK','TOTAL_REVIEWS','POSITIVE_REVIEWS','NEGATIVE REVIEWS','RECOMMENDATION']

        with open(f'{self.topath}\\product_reviews.csv','w') as wo:
            csv_writer = csv.writer(wo)
            csv_writer.writerow(headers)


        for file in li_files:
            pos_c,neg_c,comp_sum,fin_comp = 0,0,0,0
            with open(f'{self.frompath}\\{file}') as fp:
                file_content = fp.readlines()
            
            if(file_content != 0):
                prod_link = file_content[0]
                file_cont = [x for x in file_content[1:] if 'https://www.flipkart.com/' not in x]
                leng = len(file_cont)
                for rev in file_cont:
                    sent = rev.strip('\n ')
                    values = analyzer.polarity_scores(sent)
                    pos,neg,neu,comp = values['pos'],values['neg'],values['neu'],values['compound']
        
                    comp_sum+=comp
                    if pos>=neg and pos>=neu :
                        pos_c+=1
                    elif neu>=pos and neu>=neg :
                        if abs(neu - pos) > abs(neu - neg):
                            neg_c+=1
                        else:
                            pos_c+=1
                    elif neg>=neu and neg>=pos :
                        neg_c+=1
                if leng == 0:
                    leng = 1
                fin_comp = (pos_c) / (pos_c + neg_c)
                lis = [file.rstrip('.txt\n'),prod_link,leng,pos_c,neg_c,fin_comp]
    
                with open(f'{self.topath}\\product_reviews.csv','a+') as wo:
                    csv_writer = csv.writer(wo)
                    csv_writer.writerow(lis)
    
            
                


