import pandas as pd
df1=pd.DataFrame({
    "Order_ID":[1,2,3,4],
    'Customer_Name':["Rohit","Jatin","Amrit","Suhaas"]
})
df2=pd.DataFrame({
    "Order_ID":[5,6,7,8],
    "Customer_Name":["Rajpal","Khan","Paramveer","Muskan"]
})

df3=pd.concat([df1,df2],ignore_index=True)
print(df3)

df4=pd.concat([df1,df2],axis=1,ignore_index=True)
print(df4)

