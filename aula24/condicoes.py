'''condições IF, ELIF E ELSE'''

'''if é usado para verificar se uma determinada condição for verdadeira então executar um comando 
especifico, uma cadeia de blocos (comandos) especificos'''

if True: #neste caso if recebe o valor False diretamente

    nome = input('Qual é seu nome? ')
    print(f'Olá, {nome}!')


    #elif é a junção de um else e um if
    # é basicamente como se estivesse dizendo "se não for 'tal coisa', e for 'tal coisa' faça isso"
elif True:
    novo = input('Olá, você é novo aqui? ')
    print(f'Prazer em conhecê-lo')


    #else é executado caso o valor de if não seja verdadeiro, seja falso (False)
    #else não pode ser usado sozinho, depende de if
    #else śo é executado caso nenhum resultado anterior for verdadeiro (True)
else:
    print('Não te conheço')