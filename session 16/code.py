class ThingThatDoesThings:

    def __init__(self,name,multiplier=1):
        self.data=list()
        self.name=name
        self.multiplier=multiplier

    def append_datum(self,value):
        self.data.append(value)

    def execute(self):
        return list(map(lambda x:x*self.multiplier,self.data))