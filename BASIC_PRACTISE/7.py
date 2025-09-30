import pandas as pd
data={
    'Name':['Rohit','Jatin','Rahul','Mukul','Shivam','Ram'],
    'Age':[14,26,34,23,19,32],
    'City':['Mumbai','Kanpur','Delhi','Mumbai','Kanpur','Delhi'],
    'Marks':[84,68,55,74,56,35]
}
df=pd.DataFrame(data)
# print(df)
# #print(df['Name'])
# list1=['Name','Age']
# #print(df[['Name','Age']])
# print(df[list1])


# ROW FILTER
# applying consditions
# list2=df['Age']>20
# print(df[list2])

# print(df[df['Age']>20])
list3=df['Age']>20
list4=df['Marks']>40
# print(df[list3 & list4])
print(df[list3 | list4])