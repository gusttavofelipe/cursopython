
lista = [
    ('KEY1', 'value1'),
    ('KEY2', 'value2')
]

dict1 = {k.lower(): v.upper() for k, v in lista} # fazendo cast de list para dict e multiplicando valores das chaves. A variavel/valor que vem antes de ":" 
# print(dict1)                                     # será a  chave, o valor será a variavel após ":". Podem ser usadas funções nas comprehensions


dict2 = {k: v for k, v in enumerate(range(5)) } # criando dicionario com enumerate e range
# print(dict2)

dict3 = {f'key-{x}': f'value~{x**2}' for x in range(5) } # usando f-strings
print(dict3)

dict4 = {x for x in range(6)}   # se apenas uma variavel é definida, passa a ser um "set", não dicionario
# print(type(dict4), dict4)
