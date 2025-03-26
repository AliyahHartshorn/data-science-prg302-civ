def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def modulo(x,y):
    return x%y

def do_nothing(x,y):
    print("Unrecognised operation.")
    return None

functions={"+":add,"-":subtract,"*":multiply,"/":divide,"%":modulo}
num_1=float(input("x: "))
num_2=float(input("y: "))
op=input("Operation? (+ or -) ")
fn=functions.get(op,do_nothing)

answer=fn(num_1,num_2)
if answer is not None:
    print("Result is " + str(answer))