#dropna()
import pandas as pd
data={
    "Name":['Rohit',None,'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,None,45,32,23,9,67,19],
    "city":['agra',None,'mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,None,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
print(df)
df.dropna(axis=0,inplace=True)
print(df)
#axis =1 means drop row's null value
# axis =0 means colums'n null value