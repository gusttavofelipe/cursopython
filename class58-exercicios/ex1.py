
def function2():
    return "hello world"

def function1(function0):
    return function0()
    
var = function1(function2)  
print(var)