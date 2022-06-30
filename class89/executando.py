
from e_comerce.vendas import aumento, reducao
from e_comerce.formata import preco

valor = 49.90
valor_aumento = aumento(20, 100, True) # definindo como "True" o valor do parametro "formata" definido na função

valor = 49.90
valor_reduzido = reducao(20, 90, True)

print(valor_aumento)
print(valor_reduzido)

