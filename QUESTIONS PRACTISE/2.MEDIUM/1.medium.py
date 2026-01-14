import pandas as pd
import numpy as np
df = pd.read_csv(r"D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv")

df.rename(columns={'dept':'department'},inplace=True)
# print(df)
df['salary']=df['salary'].fillna(df['salary'].mean()).astype(int)
df=df.drop(columns=['join_date'])
df['annual_salary']=df['salary']*12
# print(df)



# Q8. Conditional Columns 
# 1. Create column salary_band: 
# o <40k → Low 
# o 40k–70k → Medium 
# o >70k → High 

# arr=np.array(df['salary'])
# print(arr)
# df['salary_band']=np.where(arr<40000,'Low',
#                            np.where((arr<70000), 'Medium','High'))
# print(df)


df['salary_band'] = pd.cut(
    df['salary'],
    bins=[-np.inf, 39999, 70000, np.inf],
    labels=['Low', 'Medium', 'High']
)
# # 2. Count employees per salary band 
# print(df['salary_band'].value_counts())
# print(df['salary_band'].value_counts().sort_index())


# Q9. Apply vs Vectorization 
# 1. Increase salary by 10% for IT department 

# 2. Do it: 
# o once using vectorization 
# o once using apply 
# 3. Compare performance (conceptual)

# print(df)
# df[df['department'].isin(['IT'])]['salary']=df[df['department'].isin(['IT'])]['salary']*1.10
# print(df)

# best method
# print(df)
# df.loc[df['department'] == 'IT', 'salary'] *= 1.10
# print(df)
# apply() method
# print(df)
# df['salary']=df.apply(lambda row : row['salary'] * 1.10 
#                       if row['department']=='IT' else row['salary']
#                        ,axis=1)
# print(df)


# if multiple departemtns were needed
# df['salary'] = df.apply(
#     lambda row: row['salary'] * 1.10
#     if row['department'] in ['IT'] else row['salary'],
#     axis=1
# )


# Q10. GroupBy Aggregations 
# Group by department and compute: 
# 1. Mean salary 
# 2. Max salary 
# 3. Employee count 
# 4. Total payroll 

# print(df.groupby(by='department')['salary'].mean())
# print(df.groupby(by='department')['salary'].max())
# print(df['department'].value_counts())
# print(df.groupby(by='department')['salary'].sum())


# result = df.groupby('department').agg(
#     mean_salary=('salary', 'mean'),
#     max_salary=('salary', 'max'),
#     employee_count=('salary', 'count'),
#     total_payroll=('salary', 'sum')
# )
# print(result)




# Q11. GroupBy + Filtering 
# 1. Find departments with: 
# o avg salary > 60,000 
# 2. Find departments having more than 10 employees 

df_dapertment_salary_mean=(df.groupby(by='department')['salary'].mean()>60000)
# df_dapertment_=(df['department'].value_count)
print(df[[df_dapertment_salary_mean]])



# Q12. Multi-Aggregation 
# Use agg() to compute: 
# • min salary 
# • max salary 
# • std deviation 
# per department 



# Q13. String Operations 
# On email column: 
# 1. Extract domain 
# 2. Convert to lowercase 
# 3. Check which emails belong to gmail.com 
# 4. Replace domain with company.com 




# Q14. Datetime Analysis 
# 1. Employees joined after 2020 
# 2. Employees with tenure > 3 years 
# 3. Monthly hiring count 



# Q15. Duplicate Handling 
# 1. Detect duplicate employees 
# 2. Remove duplicates keeping latest entry 
# 3. Reset index after removal 




# Q16. Data Validation 
# 1. Check if any salary is negative 
# 2. Assert no duplicate emp_id 
# 3. Validate salary column is numeric 