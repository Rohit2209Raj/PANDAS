'''
1-how big is your dtaset
2-what are the name of columns
shapes and coumns
'''
import pandas as pd
data={
    "Name":['Rohit','Rahul','Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,34,45,32,23,9,67,19],
    "city":['agra','rohtak','mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "birthday":[13,22,23,5,7,19,4,16]
}
df=pd.DataFrame(data)
print(df)
print(f'Shapes: {df.shape}')
print(f'Columns Names: {df.columns}')