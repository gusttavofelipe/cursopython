from itertools import zip_longest, count

indice = count()
city = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Santa Inês']
state = ['SP', 'MG', 'BA']
city_states = zip(state, city)  # zip junta qualquer iteravel, a variavel se torna um gerador.Com listas, associa em ordem cada valor das listas juntadas. 
                                # Retorna os valores em tuplas. a junção acontece até os itens da menor lista "acabarem"
for i, j in city_states:       
    print(i, j)   # desempacotando valores juntos com zip
    
# for i in city_states:       
#     print(i[0], i[1])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
city_states = zip(indice,state,city)  
# zip_longest junta os elementos e completa os valores com "None" caso não aja um outro disponivel)                                               
# fillvalue define um valor padrão para os valores que não possuem um elemento para fazerem junção
# utilizando zip_longest e count, nesse caso resultou em conflito que gera um loop infinito, no caso de usar count, o mais indicado é usar "zip"

for x, y, z in city_states:
    print(x,y,z)

# for i in city_states:
#     print(i[0], i[1], i[2])