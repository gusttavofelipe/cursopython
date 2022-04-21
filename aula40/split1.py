str = 'O Brasil é o país do futebol. O Brasil é penta'
list = str.split(' ')           #.split('') divide strings ao encontrar o caractere indicado na função, apaga esse caractere na divisão e
list2 = str.split('a')          # transforma em lista 

# for valor in list:  # iteração simples
#     print(valor)

for valor in list:  #iterando
    print(f'A palvara "{valor}" apareceu {list.count(valor)}x na frase') 
#.count() conta quantas vezes uma palavra/caractere/variavel indicada aparece numa str. 
# tambem é possivel fazer essa contagem iterando um item (como nesse caso)
 

