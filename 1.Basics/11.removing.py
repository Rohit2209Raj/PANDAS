import pandas as pd
data={
    "Name":['Rohit','Rahul','Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,34,45,32,23,9,67,19],
    "city":['agra','rohtak','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,7,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
# print(df)

# df.drop(coumn="Column_Name",inplace=True)
print(df)
df.drop(columns=["city","Age"],inplace=True)
print(df)