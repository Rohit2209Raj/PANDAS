import pandas as pd
# data={
#     'Name':['Rohit','Jatin','Rahul'],
#     'Age':[14,26,34],
#     'City':['Mumbai','Kanpur','Delhi']
# }
# df=pd.DataFrame(data)
df=pd.read_csv("BASIC_PRACTISE/sales_data_sample.csv",encoding="latin1")
print(df.info())