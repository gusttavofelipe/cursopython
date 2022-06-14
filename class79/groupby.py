
from itertools import groupby

studants = [
    {'nome': 'Gustavo', 'nota':'A'},
    {'nome': 'Felipe', 'nota':'C'},
    {'nome': 'Jósé', 'nota':'D'},
    {'nome': 'Luzia', 'nota':'B'},
    {'nome': 'Lorrana', 'nota':'F'},
    {'nome': 'Mariana', 'nota':'C'},
    {'nome': 'Vitor', 'nota':'E'},
    {'nome': 'João', 'nota':'C'},
    {'nome': 'Julinha', 'nota':'B'},
    {'nome': 'Julia', 'nota':'C'},
    {'nome': 'Savia', 'nota':'A'}
    ]

studants.sort(key=lambda item: item['nota']) # ordenando notas em ordem alfabetica
studants_group = groupby(studants, lambda item: item['nota']) # agrupando dicionarios pela chave 'nota'

for grupo, valores in studants_group:   # iterando sobre cada valor da chave 'nota'
    print(f'\nGrupo {grupo}:')          # printando o valor da chave 'nota'

    for notas_agrupadas in valores:
        print(notas_agrupadas)          # printando todos os grupos de notas dos dicionario em ordem alfabetica separados por groupby



