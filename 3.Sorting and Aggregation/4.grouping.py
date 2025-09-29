import pandas as pd
data={
    "Name":['Rohit',"Rahul",'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,20,30,10,30,20,40,30],
    "Salary":[1890000,980000,1165000,860000,1020000,1135000,985000,655000]
}
df=pd.DataFrame(data)
useful=df.groupby("Age")['Salary'].sum()
print(useful)
useful2=df.groupby("Age")['Salary'].mean()
print(useful2)
