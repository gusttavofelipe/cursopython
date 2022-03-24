# uma solução para o caso anterior de usar funções para retornar um valor de se é possivel ou não converter é...:
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try: # tente executar esse bloco código. semelhante aa if
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)

except: # se não der, execute esse bloco. semelhante a else
    print('Error')