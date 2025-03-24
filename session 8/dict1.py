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

names2={"one":1,2:"two",3:"three"}
for key in names2.keys():
    print(key)
val2=names2.get(1)
print(val2)