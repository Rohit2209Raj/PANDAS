import pandas as pd
data={
    "Name":['Rohit','Rahul','Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,34,45,32,23,9,67,19],
    "city":['agra','rohtak','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,7,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
#print(df)
df["Bonus"]=df['performance_score'] * 2500
# print(df) #always inserts at last

# USING INSERT METHOD
# df.insert(loc,"Col_name","data")
df.insert(1,"Surname",['raj','dev','bhardwaj','dev','singh','singh','singh','singh'])
print(df)


