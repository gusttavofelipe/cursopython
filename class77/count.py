
'''count é um contador e iterador infinito '''

from itertools import count
contador = count(start=1, step=1)  # 'start' define em qual numero inicia. 'step' define de quanto em quanto será feita a contagem (incluindo numeros negativos)
# print(next(contador))
# print(next(contador))

for value in contador: # a cada iteração os valores são 'gastos' e não se repetem de novo
    print(value)
    if value >= 10:
        break

lista = ['gustavo', 'felipe', 'silva'] 
lista = zip(contador, lista) # os valores do contador(count) continuam de onde os valores do laço for pararam                                                      
print(list(lista))