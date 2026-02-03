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

import pandas as pd
import numpy as numpy

df=pd.read_csv('D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv')
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


# df=df.rename(columns={'dept':'department'})

# df['salary_annual']=df['salary']*12

# df=df.drop(columns=['join_date'])

# df=df[['emp_id','department','name','salary','salary_annual']]
# print(df.head(2))


# Q3. Indexing & Selection 
# 1. Select only name and salary 
# 2. Select employees earning > 60,000 
# 3. Select rows with index 5 to 10 
# 4. Select employees in HR or IT 

# print(df[['salary','name']])

# print(df[df['salary'] > 60000])

# print(df.iloc[5:11])
# print(df.iloc[[5,6,7,8,9,10]])

# # print(df[(df['dept']=='HR') | (df['dept']=='IT')])
# print(df[df['dept'].isin(['HR','IT'])])

# Q4. Sorting & Ranking 
# 1. Sort employees by salary (descending) 
# 2. Rank employees by salary (dense ranking) 
# 3. Find top 5 highest paid employees 


# df['salary']=df['salary'].fillna(df['salary'].mean())
# df=df.sort_values(by='salary',ascending=False)
# print(df)

# df['salary_rank']=df['salary'].rank(method='dense',ascending=False).astype(int)
# print(df)

# top5 = df.nlargest(5, 'salary')
# print(top5)


# Q5. Missing Values 
# Given missing salaries and departments: 
# 1. Count missing values per column 
# 2. Fill salary NaNs with median 
# 3. Drop rows where department is missing 
# 4. Forward-fill remaining NaNs 

# print(df.isnull().sum())
# df=df.fillna(df['salary'].mean())


# df = df.dropna(subset=['dept'])
# print(df)

# df['salary'] = df['salary'].ffill()

# Q6. Value Counts & Unique 
# 1. Count employees per department 
# 2. Find number of unique departments 
# 3. Get department names sorted alphabetically

# print(df.groupby(by='dept')['name'].count())
# BETTER METHOD
# print(df.groupby('dept').size())
# lst=df['dept'].unique()
# print(len(lst))

# print(df['dept'].nunique())
# df = df.sort_values(by='dept')

# print(df)


# Q7. Data Type Conversion 
# 1. Convert join_date to datetime 
# 2. Extract year, month, day 
# 3. Convert salary to integer 

# df['join_date'] = pd.to_datetime(df['join_date'], dayfirst=True, errors='coerce')

# df['join_year'] = df['join_date'].dt.year
# df['join_month'] = df['join_date'].dt.month
# df['join_day'] = df['join_date'].dt.day

# print(df)












