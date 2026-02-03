import pandas as pd
import numpy as np

df=pd.read_csv(r'D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv')
df['salary']=df['salary'].fillna(df['salary'].mean())
df['salary']=df['salary'].astype(int)

# # Q8. Conditional Columns 
# # 1. Create column salary_band: 
# # o <40k → Low 
# # o 40k–70k → Medium 
# # o >70k → High 

# df['salary_category']=pd.cut(
#     df['salary'],
#     bins=[-np.inf,39999,69999,np.inf],
#     labels=['Low','Medium','High']
# )
# print(df)
# # 2. Count employees per salary band
# print(df.groupby(by='salary_category').size())

# Q9. Apply vs Vectorization 
# 1. Increase salary by 10% for IT department 
# 2. Do it: 
# o once using vectorization 
# o once using apply 
# 3. Compare performance (conceptual) 
# print(df)
# # df[df['dept']=='IT']['salary'] = df[df['dept']=='IT']['salary']*1.10 will never work
# # ALWAYS TO CHANGE IN ORGINAL DATA FRAME USE .LOC

# '''
#     df.loc[condition, column] = value
# '''
# # df.loc[df['dept']=='IT','salary']*=1.10


# print()
# print(df)
# using .apply


'''
Q10. GroupBy Aggregations 
Group by department and compute: 
1. Mean salary 
2. Max salary 
3. Employee count 
4. Total payroll

'''

# print(df.groupby(by='dept')['salary'].mean())
# print(df.groupby(by='dept')['salary'].max())
# print(df.groupby(by='dept').size())
# print(df.groupby(by='dept')['salary'].sum())

# result = df.groupby('dept').agg(
#     mean_salary=('salary', 'mean'),
#     max_salary=('salary', 'max'),
#     employee_count=('salary', 'count'),
#     total_payroll=('salary', 'sum')
# )

# print(result)
'''
Q11. GroupBy + Filtering 
1. Find departments with: 
o avg salary > 60,000 
2. Find departments having more than 3 employees 

'''

# mean_salary=df.groupby(by='dept')[['salary']].mean()
# both same
# print(mean_salary.loc[mean_salary['salary']>60000]) 
# print(mean_salary[ mean_salary['salary'] > 60000 ].index.tolist()) if want with name

# employee_count=df.groupby(by='dept').size()
# print(employee_count)
# print((employee_count[employee_count>3]).index.tolist())

'''
# # # Q12. Multi-Aggregation 
# # # Use agg() to compute: 
# # # • min salary 
# # # • max salary 
# # # • std deviation 
# # # per department 

# '''

# print(df.groupby(by='dept').agg({
#     'salary':['min','max','std']
# }
# ))

'''
# Q13. String Operations 
# On email column: 
# 1. Extract domain 
# 2. Convert to lowercase 
# 3. Check which emails belong to gmail.com 
# 4. Replace domain with company.com
# '''

# df['email']=(df['name']+'@gmail.com').astype(str)
# domain_employee=df['email'].str.split('@').str[1]
# # print(domain_employee)

# df['email']=df['email'].str.lower()

# print(domain_employee[domain_employee=='gmail.com'])

# # print(df)

# df['email']=df['name']+'company.com'
# print(df)


# '''
# Q15. Duplicate Handling 
# 1. Detect duplicate employees 
# 2. Remove duplicates keeping latest entry 
# 3. Reset index after removal 
# '''
# # display names
# print(df[df.duplicated(subset='name',keep=False)])

# # drop duplicates
# df=df.drop_duplicates(subset='name',keep='last')
# print(df)

# df = df.reset_index(drop=True)


'''
Q16. Data Validation 
1. Check if any salary is negative 
2. Assert no duplicate emp_id 
3. Validate salary column is numeric 

'''
if (df['salary'] < 0).any():
    print("There are negative salaries!")
else:
    print("No negative salaries.")




















