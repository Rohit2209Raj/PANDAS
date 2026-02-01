import pandas as pd
import numpy as np
data={
    'Name':['Rohit','Raj','Sham','Ram','Karan'],
    'Salary':[45000,18000,23000,96000,7400],
    'Dept':['IT','HR','IT','Sales','IT'],
    'Gender':['M','F','M','M','F'],
    'Experience':[10,12,3,5,8]
}

df=pd.DataFrame(data)

# print(df)
print(df.groupby(by=['Dept','Gender']).agg({
    'Salary':['mean','max','min'],
    'Experience':['mean']
}))