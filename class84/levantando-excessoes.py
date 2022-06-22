

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('ValueError: n2 não pode ser zero') # usando raise é possivel personalizar uma excessão
    return n1/n2
    
try:
    print(divide(23,0)) # a função retornará a excessão modificada sempre que for verdadeira
except ValueError as e:
    print(e)
try: 
    print(23/0) # não é possivel usar a excessão modificada fora da função
except Exception as e:
    print(e)
