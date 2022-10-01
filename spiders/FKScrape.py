import scrapy
from scrapy.crawler import CrawlerProcess
from googletrans import Translator
import re,os
import sentiment
import sort

to_file = ""

class FkscrapeSpider(scrapy.Spider):
    name = 'FKScrape'
    allowed_domains = ['www.flipkart.com']
    
    def start_requests(self):
        with open(to_file,'r') as f:
            for link in f:
                yield scrapy.Request(url = link.strip('\n'), callback=self.parse)

    def parse(self, response):
        prod_review = response.xpath('//div[@class="col JOpGWq"]/a/@href').extract_first()
        yield scrapy.Request(url = response.urljoin(prod_review), callback = self.parse_reviews)
    
   
    def parse_reviews(self,response):
        prod_name =  response.xpath('//div[@class="_1AtVbE col-10-12"]/div[@class="_2s4DIt _1CDdy2"]/text()').extract()[0] 
        prod_review = response.xpath('//p[@class="_2-N8zT"]/text()').extract() 
        prod_rev_url = response.url

        try:
            with open(f'{os.path.join(os.getcwd(),"Files")}\\{prod_name}.txt','a') as f:    
                f.write(f"{prod_rev_url}\n")
        except:
            pass

        prod_rev_stripped = [x.strip('\n ') for  x in prod_review]
            
        str = ""
        for rev in prod_rev_stripped:
                str = rev
                try:
                    with open(f'{os.path.join(os.getcwd(),"Files")}\\{prod_name}.txt','a') as f:
                        transtext = re.sub("[^A-Za-z0-9]+"," ",str)
                        f.write(transtext + "\n")
                except:
                    print("TRANSLATING.....")
                    print(str)
                    translator=Translator()
                    try:
                        translated=translator.translate(str)
                        transtext = re.sub("[^A-Za-z0-9]+"," ",translated.text)
                        print(transtext)
                        with open(f'{os.path.join(os.getcwd(),"Files")}\\{prod_name}.txt','a') as f:
                            if transtext != "" or transtext != " ":
                                f.write(transtext + "\n")
                    except:
                        str = ""
                        continue
                    str = ""
                    continue
                str = ""             
        try:
            next_page = response.xpath('//nav[@class="yFHi8N"]/a[@class="_1LKTO3"]/@href').extract()[-1]
            if next_page is not None :
                yield scrapy.Request(url = response.urljoin(next_page), callback = self.parse_reviews)
        except:
            pass

# Run the Spider
class FKScrape:
    def __init__(self,path):
        global to_file
        to_file = path
        try:
            os.mkdir(os.path.join(os.getcwd(),"Files"))
            os.mkdir(os.path.join(os.getcwd(),"CSV_Files"))
        except:
            pass
        process = CrawlerProcess()
        process.crawl(FkscrapeSpider)
        process.start()

        obj = sentiment.SentimentAnalysis(os.path.join(os.getcwd(),"Files"),os.path.join(os.getcwd(),"CSV_Files"))

        obj1 = sort.Sort()


