
'''Um módulo é um arquivo python contendo funções e
 comandos para serem usados em outros arquivos python'''

def dblist(list): # dobra os valores de uma lista
    return [x*2 for x in list]

def multiplica(list): # multiplica os valores da lista
    c = 1
    for i in list:
        c *= i
    return c

def media(list): # média da soma dos numeros da lista
    c = 0
    for i in list:
        c += i
    return c / len(list)

if __name__ == '__main__': # definindo que: se o arquivo for executado diretamente (como __main__), as funções serão executadas, caso contrario, não.
    lista = [1,2,3,4,5]
    print(multiplica(lista))
    print(dblist(lista))
    print(media(lista))
    print(__name__)
