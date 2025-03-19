# examples of pandas string manipulation
import pandas

def split_str(str):
    return str.split()

#The path below will probably be wrong. Right click the "text.txt" file
#in your VS Code explorer and copy relative path. Paste and escape any backslashes.
df=pandas.read_csv("session 7\\address.csv")

df["concat"]=df["Number"].astype(str) + df["Street"]
print(df)

df["split"]=df["Street"].apply(lambda str:str.split())
df["split2"]=df["Street"].apply(split_str)
print(df)