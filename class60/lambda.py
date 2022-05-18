'''expressões lambda: '''

# a = lambda b, c: b * c    # depois de atribuir 'lambda' a variavel, depois serão setados (não obrigartoriamente) os argumentos recebidos 
# print(a(3*5, 2))          # não se usa return, o que vem depois de ":" será o retornado


#--------------------------------------
# ordenando listas

ls = [
    ['produto1', 95],
    ['produto2', 65],
    ['produto4', 109],
    ['produto3', 5],
    ['produto5', 100],
]

''' exemplo de usabilidade.
    invés de criar uma função comum...


def funcao(item):
    return item[1]
ls.sort(key=funcao, reverse=True)


    uma expressão a lambda seria mais pratica
'''

# ls.sort(key=lambda item: item[1])   # .sort(key= recebendo como valor uma função que retorna um argumento setando índice [1]) ordena-a em ordem crescente-
# print(ls)                           # (no caso) de acordo com o valor do produto.
                                      # acrescentando 'reverse='recebendo valor True, ordenará a lista em ordem reversa 

print(sorted(ls,key=lambda i: i[0]))    # outra maneira de ordenar listas, sem que modifique a lista original
print(ls)                               # para ordenar pelo nome dos produtos, altere o valor do indice para zero


