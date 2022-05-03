'''validando CPF
168.995.350.09
---------------------------------------------------
'''
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    new_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
            
        total += int(new_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            
            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)

    if cpf == new_cpf:
        print('Válido')
        print('')
    else:
        print('Inválido')
        print('')