
def fb(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return f'{n} fizzbuzz'
    if (n % 3 == 0):
        return f'{n} fizz'
    if (n % 5 == 0):
        return f'{n} buzz'
    return n 

from random import randint

for i in range(0, 100):
    numbers = randint(0, 100)
    print(fb(numbers))