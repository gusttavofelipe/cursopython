
'''para usar for em list comprehension deve-se declarar antes e depois de for a variavel que sera usada para armazenar o valor'''

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [var for var in l1]
# print(ex1)
ex2 = [v * 2 for v in l1]   # multiplicando cada numero da lista (l1) por 2
# print(ex2)
ex3 = [(v1, v2) for v1 in l1 for v2 in range(3)]    # apresentando numeros em tuplas (estilo cordenadas)
# print(ex3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

l2 = ['Gustavo', 'Felipe', 'Elane']
ex4 = [v4.replace('a', '@') for v4 in l2]   # para cada valor, será substituido 'a' por '@'
# print(ex4)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

tupla = (
    ('valor1', 'chave1'),
    ('valor2', 'chave2'),
    ('valor3', 'chave3')
)

ex5 = [(k, v) for v, k in tupla]    # invertendo chaves e valores da tupla (tupla)
# print(ex5)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

l3 = list(range(100))
ex6 = [v5 for v5 in l3 if v5 % 3 == 0 if v5 %  8 == 0]  # checando e exibindo os numeros diviseis por 3 e 8 em l3
ex7 = [v6 if v6 % 3 == 0 and v6 % 8 == 0 else 'X' for v6 in l3]
# print(ex7)

# para usar if em comprehension não é necessario virgula, ou qualquer caractere separardor, apenas dê espaço e informe a condição
# para usar else (da mesma forma) apenas dê espaçamento e defina oq será feito caso a condição não for verdadeira
