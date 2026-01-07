import pandas as pd
def fun(marks):
    if marks>=80:
        return 'A'
    elif marks>=60 & marks<80:
        return 'B'
    else:
        return 'C'
data={
    'Name':['Rohit','Jatin','Rahul','Mukul','Shivam','Ram'],
    'Age':[14,26,34,23,19,32],
    'City':['Mumbai','Kanpur','Delhi','Mumbai','Kanpur','Delhi'],
    'Marks':[84,68,55,74,56,35]
}
df=pd.DataFrame(data)
# print(df)

# Two ways to insert
#1
# df['grade']=df['Marks']>50
df['Grade']=df['Marks'].apply(fun)

# print(df)

# Using insert method
df.insert(1,'Surname',["singh","singh","singh","singh","singh","singh"])
print(df)