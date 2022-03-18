nome = 'Gustavo'
idade = 17
altura = 1.75
peso = 52
imc = peso / altura ** 2
ano_atual = 2022
ano_de_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.1f} de altura e pesa {peso}kg')
print(f'o IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_de_nascimento}')