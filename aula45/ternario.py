
idade = input('Qual a sua idade?: ')

if not idade.isnumeric:
    print('Digite sua idade corretamente')
else:
    idade = int(idade)
    de_maior = idade >= 18
    msg = 'Acesso permitido' if de_maior else 'Acesso negado'
    print(msg)