
'''Aumento percentual'''

def increase(value, percentual):
    print((value + (value * percentual) / 100))
    return(value + (value * percentual) / 100)

increase(50, 10)
increase(12, 100)
increase(19, 13)