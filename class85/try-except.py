
# usando try except em funções e usando valor como condicional

from builtins import ValueError

def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:
    n = converte(input('digite um numero: '))

    if n is None: # definindo "is None" como parametro, pois se o valor desejado em try except não for retornado, a função retornara por padrão None
        print('Isso não e um numero\n')
    else:
        print(f'{n*2}\n')