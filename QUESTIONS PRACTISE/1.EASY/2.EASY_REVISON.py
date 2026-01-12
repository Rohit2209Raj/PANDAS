import pandas as pd
df = pd.read_csv(r"D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv")
df['salary']=df['salary'].fillna(df['salary'].mean()).astype("int")

# rename dept -> department
df.rename(columns={'dept':'department'},inplace=True)




# Creating annual_salary = salary*12
# df['annual_salary']=df['salary']*12


df.insert(4,"annual_salary",12*df['salary'])

df=df.drop(columns={'join_date'})
print(df)
print()

df=df[['emp_id','department','name','salary','annual_salary']]
print(df)