
secreto = 'antropofago'
digitadas = []  #lista vazia
chances = 8

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Isso não vale... Digite apenas uma letra')
        continue  #volta pro inicio do laço

    digitadas.append(letra)  #adiciona o valor inserido em 'letra' no final da lista 'digitadas'

    if letra in secreto:
        print(f'Boa! "{letra}" está na palavra secreta')
        print()
    else:
        print(f'Poxa! "{letra}" não está na palavra secreta')
        print()
        digitadas.pop()  #pop() remove o ultimo valor da lista

    temporario = ''
    for ltr_secreta in secreto:
        if ltr_secreta in digitadas:
            temporario += ltr_secreta
        else:
            temporario += '*'

    if temporario == secreto:
        print('CONGRATULATIONS, YOU WINSS  :)')
        print(f'A PALAVRA SECRETA É: {secreto}')
        break
    else:
        print(f' Palavra secreta: {temporario}')
        print()
    if letra not in secreto:
        chances -= 1
        print(f'Você tem {chances} chances')
    if chances == 0:
        print('Você perdeu  :(')
        break