    #criado funções

'''para se criar uma função usa-se 'def' seguido do nome escolhido para a função que obrigatoriamente precisa ter "()" no final, após isso, dois pontos e na proxima linha, respeitando a identação, faça o que você quer que sua função execute'''

def funcao():
    print('olá')
    a = input('>>> ')
# funcao()

'''pode-se criar funções que comportam outras variaveis e dar valor (inclusive diferentes) a elas.
   quando utlizadas: deve-se inserir sempre todos os valores na função de acordo com a quantidade de variaveis criadas dentro da função e seguindo sua ordem respectiva'''

def funcao2(msg, nome):
    print(msg, nome)
# funcao2('hello', True)
# funcao2('oi', 'Gustavo')
# funcao2('Neymar', 24)
# funcao2('Minecraft', 1.19)

'''pode-se colocar valores padrões as variaveis criadas na função. o valor padrão será exibido quando algum valor não for especificado na função.
   se apenas parte dos valores (em relação a quantidade de variaveis da função) forem especificados, as variaveis restantes tambem receberão valores padões
   é possivel tambem setar outro valor para as variaveis na função '''

def funcao3(msg = 'Olá', nome = 'Usuário'):
    msg = msg.lower().replace('o', '0') #replace troca o caractere indicado no primeiro argumento pelo indicado no segundo argumento
    nome = nome.replace('o', '0')
    print(msg, nome)
# funcao3(nome = 'Gustavo', msg = 'Oi')
# funcao3('Messi')
# funcao3(7, 'Cr7')
# funcao3()

''''''



