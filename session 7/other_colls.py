#using a list as a stack (LIFO queue)
sim_stack=list()
sim_stack.append("One")
sim_stack.append("Two")
sim_stack.append("Three")
print(sim_stack.pop())
print(sim_stack.pop())
print(sim_stack.pop())
#using a list as a FIFO queue
sim_fifo=list()
sim_fifo.insert(0,"One")
sim_fifo.insert(0,"Two")
sim_fifo.insert(0,"Three")
print(sim_fifo.pop())
print(sim_fifo.pop())
print(sim_fifo.pop())

#A stack in action: use your debugger to look
#at the call stack while you step into these functions.
def function1():
    f1_var="Hello"
    print("In function 1")
    function2(f1_var)
    print("Resuming context for f1")

def function2(f1_param):
    print("In function 2: " + f1_param)


function1()
print("Resuming context")
