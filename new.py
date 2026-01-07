import pandas as pd
data={
    "Country":['China','India','Pakistan'],
    "People":[101,105,100]
}
df=pd.DataFrame(data,index=['A','B','C'])
print(df)
df.reset_index(inplace=True)
print(df)
