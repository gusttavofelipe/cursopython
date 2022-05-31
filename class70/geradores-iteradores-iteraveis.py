
'''geradoes, iteradores e iteraveis'''

lista = [1,2,3,4,5]
print(hasattr(lista, '__iter__')) # a função hasattr() com segundo argumento definido ('__iter__') checa se o argumento indicado é ou não iteravel
print(hasattr(lista, '__next__')) # a função hasattr() com segundo argumento definido ('__next__') checa se o argumento indicado é ou não um iterador

lista = iter(lista) # iter() torna a variavel um iterador
print(hasattr(lista, '__next__'))   

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
lista2 = list(range(10))
print(sys.getsizeof(lista2)) # sys.getsizeof() do modulo sys, permite checar quanto uma variavel ocupa de espaço, em bytes

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# GERADOR

def generator():
    for n in range(100):
        yield n # invés de usar return, numa função iteradora usa-se yeld
g = generator()
# for v in g:
#     print(v)
    
print(hasattr(g, '__iter__'))   # geradoes são tanto iteraveis
print(hasattr(g, '__next__'))   # quanto iteradoes

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

print(next(g)) # a função next retorna um valor por vez do iteravel atribuido a ela
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

lista3 = [x for x in range(10)]
print(lista3)
lista3 = (x for x in range(10)) # tornando uma lista em gerador com list comprehension, apenas troca-se os colchetes por parenteses
print(lista3)

'''Diferença de memoria usada de um gerador para uma lista'''
lista4 = [w for w in range(10000)]
print(sys.getsizeof(lista4))
lista4 = (w for w in range(10000))
print(sys.getsizeof(lista4))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

