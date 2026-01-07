import pandas as pd
data={
    "Name":['Rohit',"Rahul",'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,18,45,32,23,9,67,19],
    "city":['agra','Patne','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,5,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
# print(df)
df.sort_values(by="performance_score",ascending=False,inplace=True)
print(df)
print("<-------------------------------->")
print()
df.sort_index(inplace=True) # just sahi kardiya data frame ko
print(df)
