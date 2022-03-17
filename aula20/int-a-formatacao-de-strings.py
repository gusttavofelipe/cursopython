nome = 'Gustavo'  #str
idade = 17  #int
altura = 1.75  #float
peso = 52  #int
imc = peso / altura ** 2

#invés de usar virgulas e aspas para delimitar oq é oq, um tipo de formatação de STRING melhor é:
print(f'{nome} tem {idade} anos de idade, tem {altura} de altura, pesa {peso} kg e seu IMC é {imc:.2f} kg')

#colocando um f antes da abertura da string e usando as variaveis entre parenteses
#e para reduzir casas decimais de numeros basta: adicionar dois pontos (:) a variavel, acrescentar mais um ponto,
#indicar com um numero quantas casas decimais quer q exiba e junto por um f para sinalizar q é um numero float


#uma outra forma de formatação é:
print('{} tem {} anos de idade, tem {} de altura, pesa {} kg e seu IMC é {:.2f} kg'.format(nome, idade, altura, peso, imc))

#invés de especificar as variaveis por seus nomes, é colocado parenteses no lugar e depois da aspa de fechamento usa-se
#a função .format(nomes das variaveis em ordem) especificando os nomes das variaveis na ordem em que devem ser inseridas
#na string.

#pode-se tbm indicar as variaveis com numeros na msm ordem em que foram colocadas. caso queira repetir as
#variaveis, basta colocar seu numero {começando por 0} na ordem ou tambem nomear as variaveis. exs a seguir

print('{0} tem {1} anos de idade, tem {2} de altura, pesa {3} kg e seu IMC é {4:.2f} kg'.format(nome, idade, altura, peso, imc))

print('{n} tem {i} anos de idade, tem {a} de altura, pesa {p} kg e seu IMC é {j:.2f} kg'.format(n=nome, i=idade, a=altura, p=peso, j=imc))

# pode-se reduzir as casas decimais como no exemplo anterior: adicionar dois pontos (:) a variavel, acrescentar mais um
# ponto, indicar com um numero quantas casas decimais quer q exiba e junto por um f para sinalizar q é um numero float






