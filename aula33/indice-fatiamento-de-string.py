'''
String indices
Fatiamento de strings [inicio: fim:passo]
'''

#indice:
#cada letra da string representa um indice, um numero e pode ser
#exibido, mechido etc, individualmente como exibido abaixo

#positivo [012345678]
texto  =  'Python_S2'
#negativo -[987654321]
print(texto [2])
input()
print(texto [-2])
input()

#Fatiamento de string
str = texto
print(str[0:6])
input()
'''
0 indice de onde eu quero começar a str
: indicador
6 até onde eu quero que vá a str
'''

#fatiando em sequencia
print(str[0::2])
input()
'''
0 de onde eu quero que comece
:algum numero: até onde eu quero que a str vá (pod-se deixar vazia tbm indicando a str completa)
2 de quanto em quanto eu quero que "pule"
'''

print(str [:])  # sem caractere de orientação a str é exibida por completo



