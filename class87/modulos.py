
import sys # importando modulo inteiro
print(sys.platform) # quando se importa o modulo inteiro, usa-se: nome do modulo + . + nome da função que deseja utilizar

from sys import platform # importanto apenas uma função
print(platform) # quando se importa a função especifica, usa-se apenas o nome da função

from sys import platform as plt # importanto função e dando a ela outro nome usando "as"
print(plt)

import random
print(random.randint(0,10))

from random import * # outra maneira de importar o modulo inteiro 

from random import randint

from random import randint, random # importando mais de uma função do modulo. apenas usa-se uma virgula para separação

def randint(*args): # uma função criada com o nome de uma função importada, sobrescreve-a
    return '>>>'

for i in range(10):
    print(randint(0,10))

''' para instalar e usar modulos externos, instale via terminal com: "pip install+nome do modulo" '''