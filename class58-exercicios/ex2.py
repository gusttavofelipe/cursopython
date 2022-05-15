
def function1(function0, *args, **kwargs):
    return function0(*args, **kwargs)

def function2(name):
    return f'Hi, {name}'

def function3(name, salutation):
    return f'{name} {salutation}'

var = function1(function2, 'Gustavo')
var2 = function1(function3, 'Gustavo,', salutation ='Bom dia!')
print(var)
print(var2)
