import pandas as pd
# df = pd.read_csv(r"D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv")
# df['salary']=df['salary'].fillna(df['salary'].mean()).astype("int")

# # rename dept -> department
# df.rename(columns={'dept':'department'},inplace=True)




# # Creating annual_salary = salary*12
# # df['annual_salary']=df['salary']*12


# df.insert(4,"annual_salary",12*df['salary'])

# df=df.drop(columns={'join_date'})
# # print(df)
# print()

# df=df[['emp_id','name','department','salary','annual_salary']]
# print(df)

# df_name_salary=df[['name','salary']]
# # print(df_name_salary)

# df_salary_60k=df[df['salary']>60000]
# # print(df_salary_60k)

# df_index_5to10=df.iloc[5:11]
# # print(df_index_5to10)

# df_department_HRandIT=df[df['department'].isin(['HR','IT'])]
# # print(df_department_HRandIT)

# df_sorted_salary=df.sort_values(by='salary',ascending=False)
# # print(df_sorted_salary)

# df['salary_rank']=df['salary'].rank(method="dense",ascending=False)
# # print(df)


df2= pd.read_csv(r"D:\COLLEGE\PANDAS\QUESTIONS PRACTISE\employee_data.csv")
# print(df2)
df2=df2.drop(columns=['join_date'])
# print(df2)

print(df2.isnull().sum(axis=0))

df2['salary']=df2['salary'].fillna(df2['salary'].mean())
# print(df2)
# print()
# df2=df2.dropna(axis=0)

df2=df2.ffill()
print(df2)

