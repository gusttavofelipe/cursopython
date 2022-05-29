
strr = '012345678901234567890123456789012345678901234567890123456789'
c = 10
lista = [strr[i:i+c] for i in range(0, len(strr), c)]
returnn = '.'.join(lista)
print(lista)
print(returnn)