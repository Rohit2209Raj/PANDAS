import pandas as pd
data={
    "Name":['Rohit',None,'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,None,45,32,23,9,67,19],
    "city":['agra',None,'mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,None,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
print(df)
# INEFFECTIVE METHOD
# df.fillna(0,inplace=True)
# print(df)

# EFFECTIVE METHOD
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['performance_score'].interpolate("linear",axis=0,inplace=True)
print(df)
