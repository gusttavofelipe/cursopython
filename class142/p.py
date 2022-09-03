from zipfile import ZipFile
import os

BASE_DIR = os.path.dirname(os.path.realpath(__name__))


caminho = '/home/gustavo/projetos/pastaspython/pzip/' # caminho dos arquivos
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho): # listando arquivos
        cam_completo = os.path.join(caminho, arquivo)
        zip.write(cam_completo, arquivo) # escrevendo os arquivos na pasta zip
        print(f'{arquivo} foi compactado')


print()   
# lendo arquivos do zip
with ZipFile('arquivo.zip', 'r') as zip: 
    for arquivo in zip.namelist():
        print(arquivo)


with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall(f'{BASE_DIR}/class142/descompactado') # descompactando arquivos no caminho indicado
    print('\nArquivos descompactados com sucesso')