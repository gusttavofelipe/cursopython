
from dados import produtos, pessoas, lista
from functools import reduce

# reduce - é um acumulador, reduz um iteravel em um unico valor. 

# na função lambda definimos:
# ac - variavel acumuladora
# item - variavel que irá comportar o valor de cada iteração do iteravel

# e retornamos:
# o acumulador + valor de cada iteração, o iteravel do qual se fará acumulação, e o valor inicial da acumulação

sum_list = reduce(lambda ac, item: ac + item, lista, 0)
print(sum_list)

sum_preco = reduce(lambda ac, p: ac + p['preço'], produtos, 0) 
print(round(sum_preco / len(produtos), 2))

sum_idade = reduce(lambda ac, id: id['idade'] + ac, pessoas, 0)
print(sum_idade / len(pessoas))