'''juntando listas

1° modo: concatenação (+)
 l1 = [1, 2, 3]
 l2 = [4, 5, 6]
 l3 = l1 + l2

 print(l1)
 print(l2)
 print(l3)

2° modo: função .extend()
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  .extend(), estende(adiciona) valores ou variaveis para dentro de
print(l1)      estrututas iteraveis colocando-as no no final, (nesse caso a lista), e só pode receber um argumento

3° modo: função .append()
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.append('Gustavo') tambem adiciona valores ou variaveis no final, com o diferencial de poder usar indices para acessar
print(l1[3])         esses valores, porem isso só funciona com valores, não é possivel fazer com variaveis

4° modo: função .insert()
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.insert(2, l2)  faz a mesma função que .append() porém possibilita escolher onde colocar o indice e tambem é possível
print(l1[2])      fazer o mesmo com variaveis'''