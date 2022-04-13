#tornando range iterável

#sem list()
l1 = range(1, 10)
print(l1)

input()

#com list()
l1 = list(range(1, 10))  # list() adiciona valores a "range" para completar a "lista" de elementos de "range" sem
print(l1)                # precisar de "for in"

input()

#usando for in
for valor in l1:
    print(valor)