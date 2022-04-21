str = 'O Brasil é o país do futebol. Brasil é penta'
list = str.split(' ')

palavra = ''
contagem =  0
for valor in list:
    qtd_vezes = list.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi "{palavra}" ({contagem}x)')
    
        
    