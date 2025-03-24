import pandas
from re import search

df=pandas.read_csv("cleaning\\medical_students_dataset.csv")

def map_gender(gender_str):
    # lookup={"non-binary":"Nonbinary",
    #         "nonbinary":"Nonbinary",
    #         'nb':"Nonbinary",
    #         "n":"Nonbinary",
    #         "o":"Unspecified",
    #         "other":"Unspecified",
    #         "nale":"Male"}
    lwr=str(gender_str).lower()
    first=lwr[0]
    if (search("fem",lwr)):
        return "Female"
    if (first=="m"):
        return "Male"
    elif (first=="f"):
        return "Female"
    else:
        return gender_str
        # tx=lookup.get(str(gender_str).lower())
        # return gender_str if tx is None else tx
lookup=pandas.DataFrame()
print(df["Gender"].apply(map_gender).unique())