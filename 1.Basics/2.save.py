import pandas as pd
data={
    "Name":['Rohit','Jatin',"Rahul"],
    "age":[18,34,12],
    "city":['Nagpur','Mumbai','Bombay']
}
df=pd.DataFrame(data)
print(df)
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json",index=False)
