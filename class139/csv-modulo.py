import csv
import os

BASE_DIR = os.path.dirname(os.path.realpath(__name__)) 

with open(f'{BASE_DIR}/class139/cliente.csv', 'r') as arquivo:
    dados = list(csv.DictReader(arquivo)) # DictReader - retorna um dict ordenado
    # dados = csv.reader(arquivo) # retorna cada linha como lista
    
    for dado in dados:
        print(dado['Nome'],dado['Sobrenome'],dado['E-mail'],dado['Telefone'])
        print(dado)

#-----------------------------------------------------------------------------------------------------------------------------------
with open(f'{BASE_DIR}/class139/cliente2.csv', 'w+') as arquivo2:
    escreve = csv.writer(arquivo2, # csv.writer() - escreve no arquivo setado
    delimiter=',',
    quotechar='"',
    quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow( # escrevendo primeira linha de "cliente" em "cliente2"
    [
        chaves[0],
        chaves[1],
        chaves[2],
        chaves[3]
    ]
    )

    for dado in dados:
        escreve.writerow( # escrevendo todos os dados de "cliente" em "cliente2"
        [
            [dado['Nome']],
            [dado['Sobrenome']],
            [dado['E-mail']],
            [dado['Telefone']]
        ]
        )


