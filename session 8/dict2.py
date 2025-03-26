student={"name":"Alex","age":21}
student["unit"]="Python"
print(student)
student["unit"]=["Python","IOT"]
print(student)
# del student["unit"]
student["units"]=["IOT",'Python']
print(student)

for key in student.keys():
    print(key + "; " + str(student[key]))

# del student["unit"]
# print(student)
