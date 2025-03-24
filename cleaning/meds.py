import pandas

df=pandas.read_csv("cleaning\\medical_students_dataset.csv")
print(df["Gender"].unique())