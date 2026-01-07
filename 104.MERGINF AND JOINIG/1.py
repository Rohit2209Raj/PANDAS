import pandas as pd
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Rohit', 'Rahul', 'Jatin']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Cost': [102,245,368]
})

final=pd.merge(df1,df2,on='ID')
print(final)