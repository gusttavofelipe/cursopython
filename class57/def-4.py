
# '''variaveis globais modificadas dentro de funções não perdem seu valor "original",
#  o valor alterado só é funcional usando a função em que a variavel foi modifiacada'''

var = 'value' # original

def funcao():
    print(var) # printando original
funcao()

#-------------------------------------------

def funcao2():
    var = 'another value' # modificada
    print(var) # printando modificada
funcao2()

print(var) # printando variavel original, pois esta fora da função

#-------------------------------------------

'''para modificar tambem a  variavel "original": use o patametro global seguido do nome da variavel
     >>>>essa pratica não é recomendavel, pois pode causar comportamentos estranhos<<<<
'''

def funcao3():
    global var # indicando que a modificação será global
    var = 'another value'
    print(var)
funcao3()
print(var)

#-------------------------------------------

'''um dos problemas de modificar uma variavel em uma funcao é que: se for definido na função uma ação
para a variavel global e em seguida modifica-la, gerará um erro de tentar usar a variavel antes de cria-la (até mesmo sendoa ação, tentar printa-la)
'''

# def funcao4():
#     print(var+'oi')
#     var = 12345
#     print(var)
# funcao4()

#-------------------------------------------

'''não se pode usar uma variavel criada dentro de uma função em outra função, pois é uma variavel local.
uma das maneiras de resolver isso é deinfir uma variavel com o valor da função e depois usar a variavel como argumento da função em que deseja usar'''

def funcao5():
    var2 = 'new value' # variavel local criada
    return var2

var3 =funcao5() # definindo a função como valor de uma variavel


def funcao6(value): # nova função
    print(value)

funcao6(var3) # definindo a variavel que possui valor de outra função como argumento dessa função