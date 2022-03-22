'''
len: mostra a quantidade de caracteres inseridos, não só em str, mas tbm em outros tipos de valores
(espaços tbm contam como caractere)
# não funciona com numeros e booleanos
# print(len(usuario)) forma simples (para caso de duvida)
'''

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
print(usuario, qtd_caracteres, type(qtd_caracteres)) # o valor da quantidade de caracteres ja é convertido

if qtd_caracteres < 5:
    print('Escreva pelo menos 5 caracteres')
else:
    print('Usuário Logado')
