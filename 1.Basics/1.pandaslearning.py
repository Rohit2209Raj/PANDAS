import pandas as pd

# read data from CSV file into a datafraame
#df = pd.read_csv("sales_data_sample.csv",encoding="latin1")
#df=pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("1.Basics/sample_Data.json")
print(df)