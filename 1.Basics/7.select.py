import pandas as pd
data={
    "Name":['Rohit','Rahul','Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,34,45,32,23,9,67,19],
    "city":['agra','rohtak','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,7,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
# print(df)
# name=df['Name']
# print(name) # single column return series
# df2=df[["Name","Age"]]
# print(df2) # multiple column return dataframe


# ROWS FILTER
print("Employe with performance score more than 6")
print(df[df['performance_score']>6])

print("Employe with performance score more than 6 and age below 40")
print(df[(df['performance_score']>6) & (df['Age']<=40)])

print("Employe with performance score more than 6 or age above 40")
print(df[(df['performance_score']>8) | (df['Age']>=40)])

