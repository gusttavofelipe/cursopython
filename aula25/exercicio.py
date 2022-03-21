
'''IDADE PARA PEGAR UM EMPRESTIMO'''

nome = input('Qual é seu nome? ')
idade = int(input('Quantos anos você tem? '))
# minimo para pegar o emprestimo
idade_minima = 18

if idade >= idade_minima:
    print(f'Olá {nome}, Você pode pegar o emprestimo')
else:
    print(f'{nome}, você não tem a idade necessária para adiquirir o emprestimo')


input()


nome = input('Qual é seu nome? ')
idade = int(input('Quantos anos você tem? '))
# limitação para pegar o emprestimo
idade_menor = 20
idade_maior = 35

if idade >= idade_menor and idade <= idade_maior: # and junta duas operações, nesse caso, duas comparações
    print(f'Olá {nome}, Você pode pegar o emprestimo')
else:
    print(f'{nome}, você não tem a idade necessária para adiquirir o emprestimo')



