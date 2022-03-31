
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break  # break é semelhante a continue, porém break, a partir do
               # momento em que é verdadeiro, além do laço de repetição, PARA o bloco de códigos prinicipal também
    print(x)
    x = x + 1

    print('Acabou!')