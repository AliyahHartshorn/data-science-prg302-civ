class Student:
    _name=""
    _age=""
    _id=""

    @property
    def getName(self):
        return self._name
    def setName(self,newName):
        self._name=newName

    @property
    def getAge(self):
        return self._age
    def setAge(self,newAge):
        self._age=newAge

    @property
    def getID(self):
        return self._id
    def setID(self,newID):
        self._id=newID

    def __hash__(self):
        return hash(self._id)
    def __eq__(self, value):
        if type(value)==str:
            return value==self._id
        else:
            return value==self


student=Student()
student.setID("1234")
student.setName("Alan Bond")
student.setAge(90)