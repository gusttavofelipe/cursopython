import os
import shutil

caminho_orig = input('Iforme o caminho de origem: ')
caminho_novo = input('Iforme o caminho de destino: ')

try:
    os.mkdir(caminho_novo) 
except FileExistsError as e:
    print(f'A pasta {caminho_novo} já existe! ')

for raiz, diretorio, arquivos in os.walk(caminho_orig):
    for arquivo in arquivos:
        try:
            if '.txt' in arquivo:
                caminho_antigo = os.path.join(raiz, arquivo)
                caminho_destinado = os.path.join(caminho_novo, arquivo)

                shutil.copy(caminho_antigo, caminho_destinado) 
                print(f'arquivo {arquivo} copiado com sucesso!')

        except shutil.SameFileError:
            print('o arquivo ja existe')


            






















