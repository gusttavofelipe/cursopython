import json
from dados import *

lista = [1,2,3,4,5,6]
dados_json = json.dumps(lista) # dumps()-fazendo cast de "list" para "array" no formato json (str em python )
print(type(dados_json), dados_json)

dados_json = json.dumps(clientes_dict, indent=4) # dumps()-fazendo cast de "dict" para "object" no formato json (str em python )
print(type(dados_json), dados_json)

dicionario = json.loads(clientes_json) # loads()-fazendo cast de "object" em json para "dict" em python
print(type(dicionario), dicionario)

#-------------------------------------------------------------------------------------------------------------------------------------

with open('clientes.json', 'w') as arquivo: # dump()-convertendo e salvando arquivo "dict" em "object" em json
    json.dump(clientes_dict, arquivo, indent=4)


with open('clientes.json', 'r') as arquivo: 
    dados = json.load(arquivo) # load()-convertendo arquivo de "object" em json para "dict" em python

print()
print(type(dados), dados)