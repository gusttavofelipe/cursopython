import os

caminho = input('Digite um caminho: ') # caminho a ser percorrido
termo = input('digite um termo: ') # termo pesquisado
conta = 0

def formata_taman(tamanho): # formata tamanho do arquivo em base 1024
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if tamanho < kilo:
         texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')

for raiz, diretorio, arquivos in os.walk(caminho): # walk(caminho) - percorre caminho enviado
    print(raiz,arquivos,diretorio)
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                conta += 1
                cam_completo = os.path.join(raiz, arquivo) # mostra o caminho completo do arquivo
                # print(cam_completo)
                # print(arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo) # splitext(arquivo) desempacota/separa o nome da extensão do arquivo 
                # print(nome_arquivo, ext_arquivo, sep=' > ')
                tamanho = os.path.getsize(cam_completo) # getsize(caminho's do arquivo's) - exibe o tamanho do arquivo em bits
                print()
                print('Arquivos encontrados:', arquivo)
                print('Caminho:', cam_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_taman(tamanho))
                print(f'\n{conta} arquivo(s) encontrado(s) ')
            except PermissionError as e:
                print('Sem permissão')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido',e)
        else:
            print('Nenhum arquivo encontrado')
