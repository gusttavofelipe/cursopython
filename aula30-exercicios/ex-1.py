
numero = input('Digite um número inteiro: ')

if not numero.isnumeric():
    print(f'"{numero}" não é um inteiro')
elif int(numero) % 2 == 0:
    print(f'{numero} é Par')
else:
    print(f'{numero} é Impar')






