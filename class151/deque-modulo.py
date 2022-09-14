
# Pilha(stack) - last in, first out

livros = []
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

livros_removed = livros.pop()
print(livros, livros_removed)



#-----------------------------------------------------------------------------------------------------------------------------------------------------
from collections import deque


# Fila(deque) - first in, first out
fila = deque()

fila.append('Maria')
fila.append('Mario')
fila.append('Marinnho')
fila.append('Marinete')
fila.append('Marineuza')

for nome in fila:
    print(nome)

print(f'Saiu: {fila.popleft()}') # apaga o primeiro valor(da esquerda)
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')




#-----------------------------------------------------------------------------------------------------------------------------------------------------
from time import sleep

fila2 = deque(maxlen=5) # define numero maximo de valores
fila2.extend([1,2,3,4])
fila2.append(5)
fila2.append(6)

# quando a quantidade maxima é excedida, o primeiro valor
# é excluido para que o proximo possa entrar

for i in range(1000):
    fila2.append(i)
    # sleep(.5)
    print(fila2)


#-----------------------------------------------------------------------------------------------------------------------------------------------------

fila3 = deque()
fila3.extend([1,2,3,4,5,6])

fila3.insert(2, 'Gu') # insere valor no indice desejado
fila3.extendleft(['fe']) # adiciona um elemento por vez a esquerda da fila
fila3.appendleft('Li') # adiciona um valor a esquerda da fila
fila3.reverse() # inverte a lista
fila3.rotate(2) # move o numero de valores definido para o inicio da lista (começando do ultimo da direita)  

print(fila3.index(4, 0, 7)) # obtem o indice do valor(start, stop)
print(fila3)