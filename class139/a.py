import random
import string

inteiro = random.randint(10, 20) # gera um numero int aleatorio entre os parametros
print(inteiro)

inteiro2 = random.randrange(0, 1000, 10) # gera um numero int aleatorio usando "range"
print(inteiro2)

flutuante = random.uniform(10, 20) # gera um numero float aleatorio entre os parametros
print(flutuante)

flutuante2 = random.random() # gera um numero float aleatorio entre 0 e 1
print(flutuante2)

lista = ['Gustavo', 'Felipe', 'José', 'Amabile', 'Renata', 'Vitória']
sorteio = random.choice(lista) # seleciona um valor aleatorio de uma sequencia
print(sorteio)

sorteio2 = random.choices(lista, k=2) # seleciona dois valores aleatorios de uma sequencia (repete valores)
print(sorteio2)

sorteio3 = random.sample(lista, 2) # seleciona dois valores aleatorios de uma sequencia sem repetir valores
print(sorteio3)

random.shuffle(lista) # embaralha os valores de uma sequencia mutavel
print(lista)


# gerador de senhas aleatorio
letras = string.ascii_letters
digitos = string.digits * 3
caracteres = '!@#$%&_-' * 3
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=11))
random.shuffle([x for x in geral])

print(senha)