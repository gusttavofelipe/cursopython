#Listas: podem conter mais de um valor, suporta diferentes tipos de valores
#Esses valores são colocados entre chaves, e para separar um valor de outro, usa-se vírgula
#Para acessar um valor individual usa-se indices, o diferencial é q cada indice pode conter um valor do tamanho desejado

#           0      1      2     3      4
lista = [132434, 'Olá', True, False, 45.545]
# -        -5     -4     -3    -2      -1
lista[-3] = 'Outro valor' #é possível mudar o valor da lista usando seu indice
print(lista[-3])
print(lista[-3::-2])  #tbm é possível usar o fatiamento para mostrar mais de valor da lista
'''
nesse caso:
0 é o valor incial que será exibido
3 é o ultimo valor que será exibido
"lembrando que os valores são exibidos apenas até um número antes do indicado"
pode-se tbm exibir os valores "pulando valores":
print(lista[-3::-1])
onde: -3 é o valor incial que será exibido
:: (se) nada estiver entre os dois pontos significa que ele seguirá a sequencia linear completa
-2 é de quanto em quanto pular
'''