from time import sleep, time

''' FUNÇÃO DECORADORA 

Permite que você potencialize,modifique ou
substitua completamente a logica de uma função ou método
'''

def master(func): # recebe uma função
    def slave(*args, **kwargs): 
        print('esta decorada') # faz algo (apenas imprime, no caso)
        func(*args, **kwargs) # executando a função
    return slave # retornando função não executada

@master # decorando função
def say_hello():
    print('hello')

say_hello()

@master # decorando função
def another(msg):
    print(msg)

another('mensagem')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# funcão decoradora que checa o tempo que outra função leva para ser executada 

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função "{funcao.__name__}" '
              f'levou {tempo:.2f}ms para executar. ')
        return resultado
    return interna

@velocidade
def qualquer():
    for i in range(5):
        sleep(1)
        print(i, end='')

qualquer()
