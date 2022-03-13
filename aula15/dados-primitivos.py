'''
tipos de dados:
str - string: textos/caracteres dentro de aspas duplas nos comandos
int - inteiro: número inteiros
float - real/ponto flutuante: números decimais/números com pontos
bool - booleano/lógico: checa a lógica de algo, valores: true e false
'''


# utilizando type antes do valor do comando e colocando o valor entre parenteses é retornado o tipo do valor inserido
print('valor', type('valor'))
print(2730, type(2730))
print(27.30, type(27.30))


print(2730 == 2730, type(2730 == 2730))
"""dois sinais de igual (==) indicam uma perguta de igualdade (no caso: 2730 é igual a 2730?), os valores poderão ser
true (verdadeiro/sim) e false (falso/não)"""

# tambem podemos fazer isso com strings. ex abaixo
print('G' == 'G', type ('G' == 'G'))

# >>>letras maiusculas e minusculas são diferenciadas<<<
print('l' == 'G', type ('l' == 'G'))

# podemaos fazer a conversão de str para bool. ex abaixo: quando convertido o valor retornado é true
print('Gustavo', type('Gustavo'), bool('Gustavo'))

"""podemos fazer tambem a conversão de str para int (apenas se o valor da string for um numero inteiro). ex abaixo: 
a funçao type foi usada para retornar o tipo do valor convertido (apenas para demonstração), caso não houvesse o valor 
retornado seria 10 (que da mesma maneira seria um valor do tipo int)"""
print('10', type('10'), type(int('10')))

# tambem podemos converter str > int dessa manaeira (apenas se o valor no qual a string for convertida já seja um int)
print('gustavo', type('gustavo'), type(int('10')))

# outra conversão possivel int > float
print(10, type(10), type(float(10)))

# tambem podemos converter float > int
print(10.33, type(10.33), type(int(10.33)))






