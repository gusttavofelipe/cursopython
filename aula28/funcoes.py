# não converter o caractere inserido ja no input, pois não é possivel checar se o caractere pode ser ou não convertido

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')


# checando se o valor pode ser convertido para valor numerico.
# as funcções :
# .snumeric checa: numeros positivos e inteiros
# .isdecimal checa:
# .isdigit checa:
# fazem essa checagem e retorna um valor booleano
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isnumeric() and num2.isnumeric(): # se os valores poderem ser convertidos, serão convertidos
    num1 = int(num1) #convertendo p int
    num2 = int(num2) #convertendo p int
    print(num1+num2)

else:  # se os valores não poderem ser convertidos...
    print('Não foi possivel converter o valor para fazer a operação')








