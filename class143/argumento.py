#!/usr/bin/env python3
import sys
import os

args = sys.argv # exibe todos os argumentos
print(args) # o 1° argumento sempre será o nome do arquivo executado

qtd_args = len(args)
if qtd_args <= 1:
    print('Ausência de argumentos:')
    print('-a para listar todos os arquivos dessa pasta', sep='\t')
    print('-d para listar todos os diretorios dessa pasta', sep='\t')
    sys.exit()

arquivos = False
if '-a' in args:
    arquivos = True

diretorios = False
if '-d' in args:
    diretorios = True

for arquivo in os.listdir('.'): # exibindo arquivos
    if arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if diretorios:  # exibindo diretorios
        if os.path.isdir(arquivo):
            print(arquivo)