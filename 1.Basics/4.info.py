import pandas as pd
# df=pd.read_json("sample_Data.json")
# print("Information about data")
data={
    "Name":['Rohit','Rahul','Jatin'],
    "Age": [10,34,45],
    "city":['agra','rohtak','mumbai']
}
df=pd.DataFrame(data)
# print(df.info())
df.info()