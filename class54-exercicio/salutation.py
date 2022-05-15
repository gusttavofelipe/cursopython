
'''Saudação'''

from unicodedata import name


def salutation(name):
    name = input('Qual é seu nome?: ')
    print(f'Olá, {name}!')

salutation(name)
