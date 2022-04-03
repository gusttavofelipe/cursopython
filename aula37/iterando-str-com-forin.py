
txt = 'Python'
novo_txt = ''

for letra in txt:  # "letra" vai receber cada letra por vez de txt a cada vez que o bloco de codigo for executado
    if letra == 't':  # será checada cada letra por vez em txt
        # continue pode ser usado da mesma forma como em while
        novo_txt += letra.upper()
    elif letra == 'h':
        novo_txt += letra.upper()
        # break pode ser usado da mesma forma como em while
    else:
        novo_txt += letra  # se nenhuma condição estiver correta será adicionado a "novo_txt" uma letra por vez da variavel "python"
                           # setada pela instancia "letra"
print(novo_txt) #cuidado em qual laço posicionar o comando
