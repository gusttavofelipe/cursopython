
'''
  tuplas são iguais a listas com o diferencial de que, ao invés de colchetes usa-se
  parenteses ou apenas os proprios valores separados. tambem não a como fazer nenhum tipo de modificação depois de criada.
  para criar uma tupla com apenas 1 elemento, deve se após dele, adicionar uma virgula (,), indicando que será uma tupla
'''

t = (1,2,3,4)
# t = 1,2,3, 'Neymar'
# t = 'Neymar', 

for i in t:     # iterando 
    print(i)

print(t[2:4])   # fatiando

t2 = 5,6,7, 'Neymar'
t3 = t+t2
print(t3)     # concatenando

var1, var2, *_, var8 = t3   # desempacotando valores
print(var1, var2, var8)

t4 = (12, 24, 55, 'sdf', 'fdv') * 2    # repetindo com operador de multiplicação
print(t4)

t4 = list(t4)   # convertendo para lista
print(t4, type(t4))

t4 = tuple(t4)  # convertendo novamente para tupla
print(t4, type(t4))