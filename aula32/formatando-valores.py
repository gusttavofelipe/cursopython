'''formatando valores com modificadores

:s - strings
:d - inteiros
:f - float
:. - (número)f - quantidade de casas decimais
:  - (caractere) (> , ^ ou <) (quantidade) (tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
'''

'''quando se coloca ': seguido do tipo de valor(:s, :f, :d)'
esta-se apenas indicando o valor, não devidamente formatando'''


str = 'Gustavo'
int = 27
float = 27.0

# str
print(f'{str:s}') #
input()

# int
print(f'{int:d}')
input()

# float
print(f'{float:f}')
input()

# casas decimais
print(f'{float:.2f}')
input()

# definindo qtd de caracteres
'''
: - chamando função de formatar
0 - caractere a ser adicionado
< - direção na qual os caracteres serão exibidos (direita)
10 - quantidade de caracteres que a variavel deverá ter, não que será adicionado a mais
'''
print(f'{int:0<10}')
input()

# "^" deixa o valor da variavel ao centro
print(f'{int:0^10}')
input()

# combinando casas decimais (float) com qtd de caracteres
print(f'{int:0<10.2f}')
input()