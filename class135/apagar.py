import os

caminho_novo = input('Iforme o caminho do arquivo a ser apagado: ')

for raiz, diretorio, arquivos in os.walk(caminho_novo):
    x = False
    for arquivo in arquivos:
        print(arquivo)     
        x = arquivo
        caminho_antigo = os.path.join(raiz, arquivo)
        # print(caminho_antigo)
        caminho_destinado = os.path.join(caminho_novo, arquivo)
        # print(caminho_destinado)
          
        if '.txt' in arquivo:
            os.remove(caminho_antigo)
            print(f'Arquivo {arquivo} apagado com sucesso! ')
            arquivo = False

    if not x:
        print('Nada a ser apagado.')
