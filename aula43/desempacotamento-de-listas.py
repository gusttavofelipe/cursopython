
# lista = ['Gustavo', 'Felipe', 'Neymar']
# n1, n2, n3 = lista
'''
ao definir que alguma(s) váriavel(eis) ira receber como valor uma lista, 
a quantidade de variaveis e indices da lista devem ser iguais pra que possa ser exibido,
pois as variaveis representam os indices respectivamente
'''
# print(n2)


'''caso não queira ou não possa criar variaveis de acordo com os indices,
uma outra variavel deve ser criada acresecentando "*" como primeiro caractere do nome,
essa variavel irá comportar o restante dos valores'''


lista = ['Gustavo', 'Felipe', 'Neymar',1, 2, 3, True, False]
n1, n2, n3, *_, ultimo = lista  # como os indices são identificados respectivamente pelas variaveis, pode-se tambem mudar a "variavel com "*"" para                                               
                                # um um outro respectivo lugar, logo, a interação tambem mudará
print(ultimo)