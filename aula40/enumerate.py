
string = 'O Brasil é penta.'
lista = string.split(' ')

for numero, valor in enumerate(lista, 100):  # enumerate(): enumera elementos iteraveis (nesse caso, listas) com a primeira variavel(numero) e mostra o valor com 
    print(numero, valor)                     # a segunda variavel(valor), no laço
                                             # é possivel indicar a partir de qual numero a numeração inicie indicando um numero após separado por virgula 
                                             

