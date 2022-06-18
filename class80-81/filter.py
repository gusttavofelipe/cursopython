from mapp import produtos, pessoas, lista

'''filter - filtra itens de iteraveis fazendo comparação booleana. recebe como argumento: a funçao da qual será feita a comparação sobre 
os itens do iteravel e o iteravel'''

nova_lista = filter(lambda x: x > 5, lista) # filtrando numeros > 5
# nova_lista = [x for x in lista if x > 5] # filtrando numeros > 5 com List comprehension
print(list(nova_lista))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def filtro(produto):    # cria uma nova chave para produtos com preço > 50 podendo ser usada em filter
    if produto['preço'] > 50:
        produto[' é caro'] = True
    return True

filtro_preco = filter(lambda x: x['preço'] > 50, produtos)  # filtrando preços > 50
for preco in filtro_preco:
    print(preco)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------


def maior_idade(pessoa): # filtra idades > 55 podendo ser usada em filter
    if pessoa['idade'] >= 55:
        return True
    else:
        False

maior_idade = filter(lambda id: id['idade'] > 55, pessoas) # filtra idades > 55
for idade in maior_idade:
    print(idade)

