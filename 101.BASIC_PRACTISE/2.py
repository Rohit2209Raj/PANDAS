import pandas as pd
data={
    'Name':['Rohit','Jatin','Rahul'],
    'Age':[14,26,34],
    'City':['Mumbai','Kanpur','Delhi']
}
df=pd.DataFrame(data)
df.to_excel("Output.xlsx",index=False)

