from mapp import produtos, pessoas, lista  # importando dados de outro arquivo python

'''map recebe como argumrnto: uma função que vai ser aplicada a cada item de um iteravel, e o iteravel no qual sera aplicado a função. map retorna um iterador '''

# print(lista)
nova_lista = map(lambda x: x*2, lista)   
# nova_lista = [x*2 for x in lista]
print(list(nova_lista))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

precos = map(lambda p: p['preço'], produtos) # acessando os preços da lista (produtos) importada
for preco in precos:
    print(preco)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def reajuste(p): # reajusta valores em 5%
    p['preço'] = round(p['preço'] * 1.05, 2) 
    return p

reajustado = map(reajuste, produtos)

for produto in reajustado:  # iterando sobre valores reajustados
    print(produto)