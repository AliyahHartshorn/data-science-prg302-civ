# examples of pandas string manipulation
import pandas

def split_str(str):
    return str.split()

df=pandas.read_csv("address.csv")
#print(pandas.concat(df["Number"].str.concat(df["Street"])))
df["concat"]=df["Number"].astype(str) + df["Street"]
df["split"]=df["Street"].apply(lambda str:str.split())
df["split2"]=df["Street"].apply(split_str)
print(df)