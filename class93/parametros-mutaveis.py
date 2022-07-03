
'''NÃO é aconselhavel usar objetos mutaveis como listas como parametros padrão de funções,
pois pode resultar em comportamentos estranhos.'''

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None: # solução para tais comportamentos
        lista = []    
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)