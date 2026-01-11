# head() ,tail()
#head(n) shows first n rows by default n=5; same for last;
import pandas as pd
df=pd.read_json("1.Basics/sample_Data.json")

# print("Display first 10 rows.")
# print(df.head(10))
# print("Display last 10 rows.")
# print(df.tail(10))

print("Display last 5 rows.")
print(df.tail())