
var = ['fGustvao', 'Felipe', 'Neymar']
startswith_g = False

for valor in var:
    if valor.lower().startswith('g'):  #.startswith checa se um valor começa com o caractere indicado
        startswith_g = True            #.lower transforma os caracteres de uma str para minusculo
        continue
    print(valor)

''' !! atenção quando for utilizar 'else' num laço 'for', checar se de fato faz sentido'''
