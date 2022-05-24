print('__________________________\n\n  PERGUNTAS E RESPOSTAS\n__________________________')
perguntas = {
    'pergunta 1' : {
        'pergunta' : 'Quanto é 2+2? ',
        'respostas' : {'a' : '1', 'b' : '4', 'c' : '5'},
        'resposta_certa' : 'b',
    },    
    'pergunta 2' : {
        'pergunta' : 'Quanto é 3*2? ',
        'respostas' : {'a' : '4', 'b' : '10', 'c' : '6'},
        'resposta_certa' : 'c',
    },
    'pergunta 3' : {
        'pergunta' : 'Quanto é 4/2? ',
        'respostas' : {'a' : '4', 'b' : '2', 'c' : '1'},
        'resposta_certa' : 'b',
    },
    'pergunta 4' : {
        'pergunta' : 'Quanto é 6**2? ',
        'respostas' : {'a' : '42', 'b' : '66', 'c' : '36'},
        'resposta_certa' : 'c',
    },
    'pergunta 5' : {
        'pergunta' : 'Quanto é 7*3**2%4? ',
        'respostas' : {'a' : '4', 'b' : '3', 'c' : '7'},
        'resposta_certa' : 'b',
    },
}
print()
rigth_answers = 0

for qk, qv in perguntas.items():
    print(f'{qk}: {qv["pergunta"]}')

    print('Opções: \n')
    for ak, av in qv['respostas'].items():
        print(f'[{ak}]: {av}')

    print()
    user_response = input('Sua resposta: ')

    if user_response == qv['resposta_certa']:
        print('Correta! ')
        rigth_answers += 1
    else:
        print('Incorreta')
    print('-----------------------------------------------')
    print()

numb_questions = len(perguntas)
perc_corret = rigth_answers / numb_questions * 100

print(f'Você acertou {rigth_answers}/{numb_questions} perguntas.')
print(f'Sua porcentagem de acerto é {perc_corret}%')
