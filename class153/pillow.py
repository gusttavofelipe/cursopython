import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

def main(pasta_imgs, nova_largura):
    if not os.path.isdir(pasta_imgs):
        raise NotADirectoryError(f'{pasta_imgs} não existe')
    
    for raiz, pasta, arquivos in os.walk(pasta_imgs):
        for arquivo in arquivos:
            cam_completo = os.path.join(raiz, arquivo)

            # retorna uma tupla com nome e extensão
            nome_arquivo, extensao = os.path.splitext(arquivo)  # desencapsulando
            tag_convertido = 'CONVERTIDO'# 'CONVERTIDO' para evitar sobrescrever 
            novo_arquivo = nome_arquivo + tag_convertido + extensao 
            cam_novo_arquivo = os.path.join(raiz, novo_arquivo)

            # if tag_convertido in cam_completo: # apaga ja convertida
            #     os.remove(cam_completo)               
            # continue 

            if os.path.isfile(cam_novo_arquivo):
                print(f'{cam_novo_arquivo} ja existe')
                continue
            
            if tag_convertido in cam_completo:
                print('Imagem ja convertida')
                continue

            img_pillow = Image.open(cam_completo)
            largura, altura = img_pillow.size # retorna largura e altura da imagem
            nova_altura = round(nova_largura * altura / largura)

            nova_imagem = img_pillow.resize((nova_largura, nova_altura), Image.LANCZOS)
            nova_imagem.save(cam_novo_arquivo, optimize=True)

            print(f'{cam_completo}: Conversão concluída')
            img_pillow.close()

            # os.remove(cam_completo) APAGA AS IMAGENS ORIGINAIS

if __name__ == '__main__':
    pasta_imgs = input('Iforme o caminho: ')
    main(pasta_imgs, 6000)