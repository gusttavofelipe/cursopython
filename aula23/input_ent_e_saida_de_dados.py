'''entrada de dados'''



#qualquer coisa digitada em input, mesmo que um numero, será retornado como string
'''input é usado para se pedir alguma informação do usuario, o argumento dentro do input deve ser uma str que será 
exibida e o usuario podera responder, é possivel atribuir uma variavel a input. ex abaixo:'''

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nascimento = 2022 - int(idade)
#como o valor retornado do input sempre é str, fazemos a conversão para podermos fazer contas em geral/usar op.lógicos

print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}.')

print()

print(f'{nome}, agora faça um pequeno exercio, descubra qual operação foi feita ')

numero1 = int(input('Digite um número: ')) #podemos fazer conversões "diretas" no input, a conversão deve vir antes do input
numero2 = input('Digite outro número: ')
numero2 = int(numero2) #tambem poodemos fazer a conversão após o valor ser digitado

print(f'O resultado é: {numero1 * numero2}')



