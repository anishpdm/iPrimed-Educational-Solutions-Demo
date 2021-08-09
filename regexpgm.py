# def sayHello():
#     print("Hello")

# x=sayHello
# x()    

def calculator(fn):
    def sayHello(x,y):
        print("Going to Add 2 numbers")
        return fn(x,y)
    return sayHello    
@calculator
def add(a,b):
    print(a+b)

add(2,5)