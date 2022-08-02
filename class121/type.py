
# criando metaclasses com type

A = type('A', (), {'atributo': 'Olá Mundo!'})
'''
A - nome da classe
() - herança
{} - dicionario como atributo
'''

a = A()
print(a.atributo)
print(type(a))