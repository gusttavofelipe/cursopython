
'''
para se criar um dicionario usa-se chaves({}) para receber todos os valores.
primeiro cria-se uma chave (um nome), a seguir dois pontos (:). e o que vier depois será o valor daquela chave.
pode-se criar mais de uma chave por variavel, basta separar por virgula ou adicionar modificando a variavel depois de craida
'''

d1  = {'chave1': f'valor1',
      'chave2': 'valor2'}

d1['chave3'] = 'valor3'         # inserindo nova chave 
d1.update({'chave4': 'valor4'}) # inserindo nova chave com funcção update
print('chave3','chave4')
print(d1['chave2'])           # para exibir o valor de uma chave especifica, usa-se seu nome como indice

#--------------------------------

# em casos de tentar uma chave que não existe, pode-se fazer uma checagem

if 'nãoexiste' in d1:
    print(d1['nãoexiste'])
print('chave não criada')

#--------------------------------

# outra forma de fazer checagem

print('chave1' in d1.keys())    #checando se à chave com o nome inserido em print
print('valor1' in d1.values())  #checando se a o valor de chave inserido em print

#--------------------------------

#checando quantos pares de chave e valor existem

print(len(d1))

#--------------------------------

# modificando valor de chave ja existente

d1['chave1'] = 'valor1 modificado'
print(d1['chave1'])

d1.update({'chave2': 'valor2 modificado'})
print(d1['chave2'])

#--------------------------------

# apagando uma chave

del (d1['chave1'])
print(d1)

d1.pop('chave4')
print(d1)

d1.popitem() #popitem apaga o ultimo item independente de qual seja

#--------------------------------

for a in d1.items():    # para acessar chaves, itere normalmente ou usando a função .keys() em d1, para acessar valores, itere usando a função .values() em d1.
    print(a[0], a[1])   # para acessar valores e chaves use a função .tems()(será retornado em tuplas)
                        # para acessar valores e chaves fora da tupla, indique o indice [0] para chave e o indice [1] para valor.
print()                 

for k, v in d1.items(): # ou, usa-se o método de desempacotamento
    print(k, v)                     

#--------------------------------
#pode-se adicionar dicionarios dentro de dicionarios

clientes = {
    'cliente1' : {
        'nome' : 'Gustavo',
        'sobrenome' : 'Silva'
    },

    'cliente2' : {
        'nome' : 'José',
        'sobrenome' : 'Silva'
    }
} 

for client_k, client_v in clientes.items():
    print(f'Exibindo {client_k}')
    for dados_k, dados_v in client_v.items():
        print(f'\t{dados_k} = {dados_v}')

#--------------------------------

#copiando dicionarios

import copy

d2 = {1 : 'a', 2 : 'b', 3 : 'c'}
v = d2
v[1] = 'Gustavo'    # quando se atribui a uma variavel um dicionario como valor, uma outra variavel não é criada , as duas, passam a ser a mesma, identicas
print(v)
print(d2)

v = copy.deepcopy(d2)   # para se 'criar' outro dicionario igual é usada a função  "copy.deepcopy()" importada de "copy"
v[4] = ['Gustavo']
print(d2)
print(v)
v[4][0] = 'Felipe'  # modificando lista dentro do dicionario
print(v)

#--------------------------------

# é possivel fazer cast de listas ou tuplas para dicionario

lista = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3)
]

dic = dict(lista)
print(dic)

#--------------------------------

# concatenando dicionarios

d3 = {
    1 : 2,
    3 : 4,
    5 : 6
}

d4 = {
    'a' : 'b',
    'c' : 'd',
    'e' : 'f'
}

d3.update(d4)
print(d3)