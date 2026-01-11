import pandas as pd
df = pd.read_csv(r"D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv")

# Q1. Data Loading & Inspection 
# Given employees.csv: 
# emp_id name dept salary join_date 
# 1. Load the dataset 
# 2. Display: 
# o shape 
# o column names 
# o data types 
# 3. Show first 3 and last 2 rows 
# 4. Find memory usage 

# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# print(df.head(3))
# print(df.tail(2))
# print(df.memory_usage())


# Q2. Column Operations 
# 1. Rename dept → department 
# 2. Create a new column salary_annual = salary * 12 
# 3. Drop join_date 
# 4. Reorder columns logically

# print(df)
# df=df.rename(columns={'dept':'department'}) #unique and good
# df['salary_annual']=df['salary']*12
# # df.drop(columns=["join_date"],inplace=True)
# df=df.drop(columns=["join_date"])
# df = df[['emp_id', 'name', 'department', 'salary', 'salary_annual']]

# print(df.head())


# Q3. Indexing & Selection 
# 1. Select only name and salary 
# 2. Select employees earning > 60,000 
# 3. Select rows with index 5 to 10 
# 4. Select employees in HR or IT

# df2=df[['name','salary']]
# print(df2.head())

# df2=df[df['salary']>60000]
# print(df2.head())

# print(df)

df2=df[df['dept']=='IT' | df['dept']=='HR]']
print(df2)
