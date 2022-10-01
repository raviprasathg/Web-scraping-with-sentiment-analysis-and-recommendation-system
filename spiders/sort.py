import pandas as pd
import os

class Sort:
    def __init__(self):
        df = pd.read_csv(f"{os.getcwd()}\\CSV_Files\\product_reviews.csv")
        df_fin = df.sort_values(by = ["POSITIVE_REVIEWS","RECOMMENDATION"], ascending = [False,False])
        df_fin.to_csv(f"{os.getcwd()}\\CSV_Files\\sorted_product_reviews.csv",index = False)
        



