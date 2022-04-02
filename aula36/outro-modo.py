
frase = 'O rato roeu a roupa do rei de roma'
tam_frase = len(frase)
contador = 0
new_str = ''
input = input('Qual letra você quer tornar Maiúscula? ')

while contador < tam_frase:
    letra = frase[contador]

    if letra == input:
        new_str += input.upper() # uuper torna a letras maiúsculas
    else:
        new_str += letra
    contador += 1  #contador está primariamente na cadeia de blocos do laço while
print(new_str)