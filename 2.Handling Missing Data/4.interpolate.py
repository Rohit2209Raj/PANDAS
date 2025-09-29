'''
10 20 30 NAN 50 60
series predict the NAN = 40
 this is what interpolate does
'''
import pandas as pd
data={
    "Name":['Rohit',"Rahul",'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,None,45,32,23,9,67,19],
    "city":['agra',None,'mumbai','pune','noida','gurgoan','panipat','jaipur'],
    "performance_score":[10,None,8,2,5,3,7,5]
}
df=pd.DataFrame(data)
print(df)
'''
interpolate methods-
1 linear
2 polynomial
3 time
'''
df.interpolate("linear",axis=0,inplace=True)
print(df)

