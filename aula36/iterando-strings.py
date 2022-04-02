
frase = 'O rato roeu a roupa do rei de roma'
tam_frase = len(frase)
contador = 0
new_str = ''

while contador < tam_frase:
    # print(frase[contador]) # o "contador" nesse caso, torna-se o indicador do indice
    # new_str += frase[contador]
    letra = frase[contador]

    if letra == 'r':
        new_str += 'R'
    else:
        new_str += letra
    contador += 1  #contador está primariamente na cadeia de blocos do laço while
print(new_str)
