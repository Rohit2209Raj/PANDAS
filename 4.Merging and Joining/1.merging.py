import pandas as pd
df1=pd.DataFrame({
    "Order_ID":[1,2,3,4],
    'Customer_Name':["Rohit","Jatin","Amrit","Suhaas"]
})
df2=pd.DataFrame({
    "Order_ID":[1,2,4,5],
    "Cost":[1200,1233,99,101]
})

df_merged=pd.merge(df1,df2,on="Order_ID",how="inner")
print("inner")
print(df_merged)

'''
if *****
****
*** show in place of name
is not a code error — it’s just how pandas displays DataFrames when your console or terminal window is too narrow to fit all columns.

So Pandas automatically compresses the output and shows ... in between columns.
'''
df_merged=pd.merge(df1,df2,on="Order_ID",how="outer")
print("outer")
print(df_merged)

df_merged=pd.merge(df1,df2,on="Order_ID",how="left")
print("left")
print(df_merged)


df_merged=pd.merge(df1,df2,on="Order_ID",how="right")
print("right")
print(df_merged)


