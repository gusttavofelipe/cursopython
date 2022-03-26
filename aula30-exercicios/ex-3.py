tamanho_do_nome = input('Informe seu nome: ')
quantidade_de_caracteres = len(tamanho_do_nome)

if quantidade_de_caracteres <= 4:
    print('Seu nome é curto')
elif quantidade_de_caracteres > 4 and quantidade_de_caracteres <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')




