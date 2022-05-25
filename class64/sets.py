
'''
set é uma especie de lista que não repete um valor adicionado em si mais de uma vez e não possui ordem. similar a um dicionario, porem não é formado por chave e valor.
um set não possui indice, não se pode acessar um valor isolado, porem, pode-se iterar sobre ele
'''

# formas de criar

set1 = {1,2,3,3,3,3,3,4,5}

for i in set1:
    print(i)

#----------------------------------
# esse modo permite definir um set vazio
# a função add só suporta um valor por vez

set2 = set( )
set2.add('Gustavo') # adicionando valor ao set2
set2.add(2)         # adicionando valor ao set2
set2.add(True)      # adicionando valor ao set2
set2.add(4)         # adicionando valor ao set2
set2.add(5)         # adicionando valor ao set2
print(set2)

#----------------------------------
# removendo um valor

set2.discard('Gustavo') # essa função tambem só aceita um argumento por vez
print(set2)

#----------------------------------
# similar a add, update, ao receber um iteravel, itera sobre ele e adiciona ao set

set2.update('Python', [236], {45,46,34})
print(set2)

#----------------------------------
#casts com set

lista = [1,1,1,1,1,1,13,3,3,3,3,'gustavo', 'gustavo']
lista = set(lista)  # cast para set, elimina os valores duplicados
lista = list(lista) # voltando cast para lista, porem, agora a lista não possui mais os elementos duplicados
print(lista)
print(lista[0:-1])

#----------------------------------
# unindo/juntando sets

set3 = {1,2,3,4,5,}
set4 = {1,2,3,4,5,6}
set5 = set3 | set4  # unindo usando pipe 
set4.union(set3)    # unindo usando função union
print(set5)
print(set4)

#----------------------------------
# interseção (elementos presentes em ambos os sets)

set3 = {1,2,3,4,5,}
set4 = {1,2,3,4,5,6}
set6 = set3 & set4  # usando & comercial
print(set6)

#----------------------------------
# diferença (elemento(s) que estão apenas em um dos sets)

set3 = {1,2,3,4,5,8}
set4 = {1,2,3,4,5,6}
set7 = set3 - set4  # a diferença será o/os valor(es) do set da esquerda que não estão no set da direita
print(set7)

#----------------------------------
# difrença simetrica (elementos que estão nos dois sets, mas não em ambos simultaneamente)

set3 = {1,2,3,4,5,8}
set4 = {1,2,3,4,5,6}
set7 = set3 ^ set4
print(set7)
