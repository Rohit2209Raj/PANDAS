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
'''
    very very very good example ad questiosn
'''

# df2=df[['name','salary']]
# print(df2.head())

# df2=df[df['salary']>60000]
# print(df2.head())


# df2=df[df['dept'].isin(['HR','IT'])]
# print(df2)

# df2=df.iloc[5:11]
# print(df2)

# Q4. Sorting & Ranking 
# 1. Sort employees by salary (descending) 
# 2. Rank employees by salary (dense ranking) 
# 3. Find top 5 highest paid employees 

'''
GOOD AND GRETA LEARNING
'''


# df.sort_values(by="salary",ascending=False,inplace=True)
# # print(df)

# df['salary_rank']=(df['salary'].rank(method='dense',ascending=False))
# print(df)

# df2=df[df['salary_rank']<=5]
# print(df2[['name','salary']])


# # Given missing salaries and departments: 
# # 1. Count missing values per column 
# # 2. Fill salary NaNs with median 
# # 3. Drop rows where department is missing 
# # 4. Forward-fill remaining NaNs
# print(df)
# print()
# print(df.isnull().sum())
# print()
# # df['salary'].fillna(df['salary'].mean(),inplace=True)
# # df.dropna(subset=['salary'],inplace=True)
# df = df.ffill()

# print(df)


# Q6. Value Counts & Unique 
# 1. Count employees per department 
# 2. Find number of unique departments 
# 3. Get department names sorted alphabetically 
# print(df)
# print(len(df['dept'].unique()))

# # df.sort_values(by="dept",ascending=True,inplace=True)
# # print(df)

# useful=df.groupby("dept")['emp_id'].count()
# print(useful)

'''
coorect and better solutino
# 1. Count employees per department
print(df['dept'].value_counts())

# 2. Number of unique departments
print(df['dept'].nunique())

# 3. Department names sorted alphabetically
print(sorted(df['dept'].unique()))

'''


# Q7. Data Type Conversion 
# 1. Convert join_date to datetime 
# 2. Extract year, month, day 
# 3. Convert salary to integer

# print(df.head())

# # df['join_date']=df['join_date'].astype('datetime64[ns]')
# df['join_date'] = pd.to_datetime(df['join_date'], format='%d-%m-%Y') #interview reccomended
# # print(df['salary'].mean())
# df['salary'].fillna(df['salary'].mean(),inplace=True)
# print(df['salary'])
# df['salary']=df['salary'].astype('int')
# print(df.head())

'''
# Convert join_date to datetime
df['join_date'] = pd.to_datetime(df['join_date'], format='%d-%m-%Y')

# Extract year, month, day
df['join_year'] = df['join_date'].dt.year
df['join_month'] = df['join_date'].dt.month
df['join_day'] = df['join_date'].dt.day

# Convert salary to integer (safe)
df['salary'] = df['salary'].fillna(df['salary'].median()).astype(int)


'''









