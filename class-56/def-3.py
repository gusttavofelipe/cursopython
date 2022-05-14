
def funcao(a1, a2, a3, a4, a5, a6=None, a7=int ):  # após setar um valor para um argumento, todos os outros que vierem após, 
    print(a1, a2, a3, a4, a5, a6, a7)              # devem tambem ter seus valores especificados

funcao(1,2,3,4,5, a6='oi', a7=21)   # a partir do momento em que se da um valor especificando a qual argumento pertence, todos os outros que vierem após
                                    # devem tambem seguir o mesmo padrão

#-----------------------------

'''Os argumentos inseridos usando *args, são armazenados em uma tupla,
não se pode modificar uma tupla. porém pode-se fazer cast de tupla para lista'''

def funcao2(*args):   # é utilizado quando NÃO se sabe a quantidade de argumentos que serão usados
    print(args)       # printando todos os argumentos
    print(args[-1])   # checando argumentos por indice
    print(len(args))  # checando quantidade de argumentos
    args = list(args) # convertendo para lista
    args[3] = 'new value' # trocando valor da lista
    print(args)
    
funcao2('oi', 1, True, 90.0 ) 

#-----------------------------

def funcao3(*args):
    print(args)

lista = [1,2,3,4,5] # quando se usa listas, tambem são armazenadas dentro tuplas
funcao3(lista, '0nz3') #argumentos inseridos junto de listas, ficam fora da lista, porem (mas ainda dentro da tupla)    
funcao3(*lista, '0nz3') # para reslover o problema acima, o recomendado é -
                        #mandar a lista desempacotada, assim os demais elementos inseridos, tambemm faram parte dela

#-----------------------------

def funcao4(*args, **kwargs): # **kwargs são dicionarios
    print(args)
    print(kwargs,type(kwargs))
    print(kwargs['nome'], kwargs['sobrenome'])   # usando indices com kwargs

    nome = kwargs.get('nome')   # outra forma de iterar sobre kwargs. usada quando não se tem certeza que o argumento setado realmente exista 
    idade = kwargs.get('idade') # caso esse argumento não exista, será retornado o valor None
    print(nome, idade)
funcao4(3434,456,667,788, nome='Gustavo', sobrenome='Felipe')
