
# criando arquivos

file = open('abc.txt', 'w+')  # 1° argumento de "open" deve ser o nome e extensão do arquivo - 2° argumento é o modo de como trataremos esse arquivo
file.write ('linha 1\n') # "write" escreve nas linhas do arquivo
file.write ('linha 2\n')
file.write ('linha 3\n')

file.seek(0,0) # "seek" desloca o cursor de leitura para posição desejada. 1° parametro: número de posições para avançar - 2° parametro: ponto de referência
print(file.read()) # "read" lê o arquivo inteiro (se não especificado os argumentos) e retorna uma str

file.seek(0,0) # deslocando cursor novamente para o inicio
print(file.readline(), end='') # "readline" lê uma linha do arquivo por vez
print(file.readline(), end='')
print(file.readline(), end='')
print()

file.seek(0,0)
print(file.readlines()) # "readlines" lê todas as linhas e as retorna em uma lista
print()

# # for linhas in file.readlines(): # iterando sobre a lista retornada (tambem é possivel iterar sobre o arquivo em si)
# #     print(linhas, end='')

file.close() # "close" fecha o arquivo 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# outra forma de criar arquivos
# utilizando ""with"" é necessario apenas abrir o arquivo e definir a variavel do qual ele será com "as"

with open('def.txt', 'w+') as file2: 
    file2.write('linha 4\n')
    file2.write('linha 5\n')
    file2.write('linha 6\n')

    file2.seek(0)
    print(file2.read())

# o arquivo é fechado automaticamente

import os
with open('def.txt', 'a+') as file2: # 'a+' adiciona novas linhas ao arquivo sem apagar os dados ja existentes
    file2.write('usando a+\n') 
    file2.seek(0)
    print(file2.read())

# os.remove('abc.txt') # apagando o arquivo com "remove"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

