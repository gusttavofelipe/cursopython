
from itertools import combinations, permutations, product
peoples = ['Gustavo', 'Felipe', 'José', 'Luzia', 'Mariana', 'Lorrana'] 

for combinats in combinations(peoples, 2):  # combinations recebe a variavel e a quantidade de 'grupos' que é solicitado para fazer a combinação. 
    print(combinats)                        # a ordem das combinações não importa 
print()
for combinats in permutations(peoples, 2):  # permutations: semelhante a combinations, porem a ordem das combinações importa
    print(combinats)
print()
for combinats in product(peoples, repeat=2):  # product: semelhante a permutations, porem um nome pode se repetir de acordo com a quantidade definida em repeat
    print(combinats)