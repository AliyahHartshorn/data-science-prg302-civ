import math

#This circle is defined as a position in space and a radius.
#In our (unrealistic) example, we're restricting the space
# to have at most one circle of each radius. We can, then,
# use the radius as a proxy unique identifier.
class Circle:
    radius=0
    centre_x=0
    centre_y=0
    def __init__(self,x,y,r):
        self.radius=r
        self.centre_x=x
        self.centre_y=y
    def calculate_area(self):
        return math.pi * self.radius**2
    
    # Because radius is proxy unique ID, we can override
    # the normal hash function to return the radius's
    # hash:
    def __hash__(self):
        return hash(self.radius)
    # But if we do that, we also need to override the ==
    # function so that we recognise a radius as an 'alias'
    # for a circle.
    def __eq__(self, value):
        if (type(value)==int):
            return value==self.radius
        elif (type(value)==Circle):
            return value.radius==self.radius
        return False

# Make a couple of circles and see that their
# instance methods are working OK:
c1=Circle(1,1,10)
print(c1.calculate_area())
c2=Circle(2,2,5)
print(c2.calculate_area())

# Now make a dictionary with those circles. This is our
# "master" list of circles.
master={c1:c1,c2:c2} 
# Before making a new circle, we can check to see if there's
# already one with that radius:
new_circle=None
if (50 in master.keys()):
    new_circle=master[50]
else:
    new_circle=Circle(1,1,50)
    master[new_circle]=new_circle

# And we can fetch our circles from the dictionary by radius:
old_circle=master[10]
print(old_circle.radius)