import pandas

df=pandas.read_csv("cleaning\\medical_students_dataset.csv")

def map_gender(gender_str):
    first=str(gender_str)[0].lower()
    if (first=="m"):
        return "Male"
    elif (first=="f"):
        return "Female"
    else:
        return gender_str
print(df["Gender"].apply(map_gender).unique())