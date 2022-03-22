'''
operadores logicos
and, or, not
in, e not in
'''

# and: faz comparação entre expressões. as duas sendo verdadeiras = true, uma ou duas falsas = false
# (a ou e são verdadeiras?)
a = 1
b = 1
print(a and b >= 1)


# or: verifica se ao menod umas das expressões é verdadeia. uma sendo verdaddeira = true, todas sendo falsas s= flase
# (a ou b são verdadeiras?)
a = 1
b = 1
print(a and b > 1)


# not: inverte a expressão, se era falso, fica true. se tal coisa era maior, vira menor. tambem podem retornar valores bool
a = 2
b = 1

print(not a > b)

if not a > b:
    print('A maior que B')
else:
    print('B maior que A')


# in: verifica se algo esta contido em algo (isto esta contido nisto?)
# se for verificar se algo esta contida numa str coloque o texto entre aspas (''), segue a mesma regra
nome = 'Gustavo Gato'
if 'Gus' in nome:
    print('Está contido na string')
else:
    print('Não está contido na string')


# not in: contrario de in. verificar se algo NÃO esta contido em algo (isto não esta contido niso?)
nome = 'Gustavo Gato'
if 'gus' not in nome:
    print('Executado')
else:
    print('Isto está contido')



