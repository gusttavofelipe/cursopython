
from e_comerce.formata import preco # importando modulo "preco" do subpacote de "e_comerce" formata

def aumento(valor, porcentagem, formata=False): # aumenta o valor do preço de acordo com a porcentagem informada. 
    r = valor+(valor*(porcentagem/100))
    if formata: # checagem para determinar o envio do parametro "formata" defindo como "False"
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=False):  # reduz o valor do preço de acordo com a porcentagem informada
    r = valor-(valor*(porcentagem/100))
    if formata: # checagem para determinar o envio do parametro "formata"
        return preco.real(r)
    else:
        return r