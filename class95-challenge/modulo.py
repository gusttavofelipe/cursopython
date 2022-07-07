import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):   # chama todas as outras funções
    cnpj = remover(cnpj)

    try:
        if sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula(cnpj=cnpj, digito=1)
        novo_cnpj = calcula(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False
        

def sequencia(cnpj): # checa se a CNPJ é uma sequencia ou não
    numeros = cnpj[0] * len(cnpj)
    if numeros == cnpj:
        return True
    else:
        return False

def remover(cnpj):  # remove da str tudo que não esta entre 0 e 9
    return re.sub(r'[^0-9]', '', cnpj)


def calcula(cnpj, digito):  # faz todos os calculos e checagens de REGRESSIVO
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None
    
    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
    
    digito = 11 - (total%11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'
