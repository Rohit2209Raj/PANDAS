import pandas as pd
data={
    'Name':['Rohit','Jatin','Rahul','Mukul','Shivam','Ram'],
    'Age':[14,26,34,23,19,32],
    'City':['Mumbai','Kanpur','Delhi','Mumbai','Kanpur','Delhi']
}
df=pd.DataFrame(data)
print(df.shape) # (columns,rows)
print(df.columns)
