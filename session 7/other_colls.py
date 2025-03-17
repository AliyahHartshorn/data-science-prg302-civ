sim_stack=list()
sim_stack.insert(0,"One")
sim_stack.insert(0,"Two")
sim_stack.insert(0,"Three")
print(sim_stack.pop())
print(sim_stack.pop())
print(sim_stack.pop())

def function1():
    f1_var="Hello"
    print("In function 1")
    function2(f1_var)
    print("Resuming context for f1")

def function2(f1_param):
    print("In function 2: " + f1_param)


function1()
print("Resuming context")
