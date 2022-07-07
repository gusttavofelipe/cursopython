
import modulo

cnpj = '70.949.572/0001-05'

if modulo.valida(cnpj):    # validando cnpj
    print(f'{cnpj} é Válido')
else:
    print(f'{cnpj} é Inválido')



for i in range(100):    # gerando cnpj
    novo_cnpj = modulo.gera()
    formatado = modulo.formata(novo_cnpj)
    print(formatado)