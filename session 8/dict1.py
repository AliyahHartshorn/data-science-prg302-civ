#This example from the week 8 slides
names={}
while True:
    name=input("Name: ")
    if name=="":
        break
    elif name in names.keys():
        temp=names[name]
        names[name]=temp+1
    else:
        names[name]=1
print(names)

# Demo KeyError, and how .get() avoids it.
names2={"banana":1,"orange":1,"loquat":1}
fruit=names2["strawberry"]
fruit=names2.get("strawberry",-1)
print(fruit)
fruit=names2.get("orange",-1)
print(fruit)
