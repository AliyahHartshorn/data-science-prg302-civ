import datetime

class Cat:

    def __init__(this,name,age,coat):
          this.name=name
          this.age=age
          this.coat=coat

          this.stomach_contains=["fish"]
          this.last_meal=datetime.datetime.now()
    
    def meow(this):
        print(this.name + " says meow")

    def eat(self,food):
        self.stomach_contains.append(food)
        self.last_meal=datetime.datetime.now()

cat=Cat("John",8,"red")