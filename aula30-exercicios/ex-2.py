saudacao = input('Digite um horário entre 0-23: ')

if saudacao.isdigit():
    saudacao = int(saudacao)
    if saudacao < 0 or saudacao > 23:
        print('Por favor digite um horário entre 0-23')
    elif saudacao <=11:
        print('Bom dia!')
    elif saudacao <=17:
        print('Boa Tarde!')
    else:
        print('Boa Noite!')
else:
    print('Por favor, digite um horário válido')