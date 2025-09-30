import pandas as pd
data={
    'Name':['Rohit','Jatin','Rahul','Mukul','Shivam','Ram'],
    'Age':[14,26,34,23,19,32],
    'City':['Mumbai','Kanpur','Delhi','Mumbai','Kanpur','Delhi'],
    'Marks':[84,68,55,74,56,35]
}
df=pd.DataFrame(data)
print(df)
if df.loc[1,'Marks']>60:
    # df.loc[1,'Age']=df.loc[1,'Age']+100
    df.loc[1,'Age']+=100
# df.loc[df['Marks']>50,'Age']=df['Age']+1
print(df)