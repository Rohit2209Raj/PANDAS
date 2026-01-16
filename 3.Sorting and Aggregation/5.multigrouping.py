import pandas as pd
# data={
#     "Name":['Rohit',"Rahul",'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
#     "Age": [10,20,30,10,30,20,40,30],
#     "Salary":[1890000,980000,1165000,860000,1020000,1135000,985000,655000]
# }

data={
    "Name":['Rohit',"Rahul",'Jatin','Mukul','Shivam','Tanya','Satyam','Ginni'],
    "Age": [10,20,30,10,30,20,40,30],
    "Salary":[1890000,980000,1165000,860000,1020000,1135000,985000,655000]
    }
df=pd.DataFrame(data)
df['Bonus']=df['Salary']*0.15
print(df)

learn=df.groupby(["Age","Name"])['Salary'].sum()
print(learn)
# useful=df.groupby(["Age","Name"])['Salary'].sum()
# print(useful)