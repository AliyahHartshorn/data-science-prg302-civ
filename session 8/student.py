class Student:
    _name=""
    _age=""
    _id=""

    def __init__(self,id,name,age):
        self._id=id
        self._name=name
        self._age=age

    def get_name(self):
        return self._name
    def set_name(self,newName):
        self._name=newName
    name=property(fget=get_name,fset=set_name)

    def get_age(self):
        return self._age
    def set_age(self,newAge):
        self._age=newAge
    age=property(fget=get_age,fset=set_age)

    def get_id(self):
        return self._id
    def set_id(self,newID):
        pass
        # self._id=newID
    id=property(fget=get_id,fset=set_id)

    def get_first_name(self):
        parts=self._name.split()
        return parts[0]
    def switch_name(self):
        parts=self._name.split()
        self._name=parts[1]+" "+parts[0]
        
    def __hash__(self):
        return hash(self._id)
    def __eq__(self, value):
        if type(value)==str:
            return value==self._id
        else:
            return value==self


student=Student("1234","Alan Bond",80)
student2=Student("1235","Andrew Forrest",79)
student3=Student("1236","Moondyne Joe",200)
student4=Student("1237","AO Neville",150)

# print(student3.get_first_name())
# print(student3.switch_name())
# print(student3.name)

student5=Student("1238","Rinehart Gina",70)
student5.switch_name()
print(student5.name)

# print(student2.id)
# print(student3.id)
# print(student3.name)
# student3.age=300
# print(student3.age)

# student_set={student:student,
#              student2:student2,
#              student3:student3,
#              student4:student4
#             }
# out_student=student_set["1235"]
# print(out_student.name)
