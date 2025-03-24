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
        self._id=newID
    id=property(fget=get_id,fset=set_id)

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

print(student3.id)
print(student3.name)
student3.age=300
print(student3.age)
