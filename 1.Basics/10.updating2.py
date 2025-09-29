import pandas as pd
data={
    "Name":['Rohit','Rahul','Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,34,45,32,23,9,67,19],
    "city":['agra','rohtak','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,7,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
print(df)

# increaing everyone age by one after 31 dec
df["Age"]=df["Age"]+1
# df[df['performance_score']>6]=df['performance_score']+100
# ValueError: Must have equal len keys and value when setting with an iterable
# Correct method
df.loc[df['performance_score'] > 6, 'performance_score'] += 100


print(df)