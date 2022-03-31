'''calculadora de calculos infinitos'''

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s] [n] ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        continue
        input()
    num1 = int(num1)
    num2 = int(num2)

        # + - * /
    if operador == '+':
        print(num1+num2)
    elif operador == '-':
        print(num1-num2)
    elif operador == '*':
        print(num1*num2)
    elif operador == '/':
        print(num1/num2)
    else:
        print('Digite um operador válido')
        input()



