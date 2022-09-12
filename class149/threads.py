from threading import Thread
from threading import Lock
from time import sleep

# Thread: processo, execução
# main Thread: processo principal     

'''
class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    
    def run(self): # reescrevendo metodo
        sleep(self.tempo)
        print(self.texto)

# executando thread da classe
t1 = MyThread('Thread1', 3)
t1.start() # inicia thread da classe

t2 = MyThread('Thread2', 2)
t2.start() 

t3 = MyThread('Thread3', 5)
t3.start() 

# executando na main thread
for i in range(10):
    print(i)
    sleep(1)
'''
# ------------------------------------------------------------------------------------------------------------------------------

# outra maneira de criar threads

'''
def demora(texto, tempo):
    sleep(tempo)
    print(texto)

# target > objeto
# args > argumentos
tf1 = Thread(target=demora, args=('Thread em função 1', 3))
tf1.start() # iniciando thread

tf2 = Thread(target=demora, args=('Thread em função 2', 1))
tf2.start() # iniciando thread

tf3 = Thread(target=demora, args=('Thread em função 3', 5))
tf3.start() # iniciando thread


for i in range(10):
    print(i)
    sleep(.5)
'''
# ------------------------------------------------------------------------------------------------------------------------------

'''
def demora(texto, tempo):
    sleep(tempo)
    print(texto)

tf1 = Thread(target=demora, args=('Thread em função 1', 5))
tf1.start() 
# tf1.join() # pausa a thread atual(main thread) até que a thread alvo termine
# print('OI')


# forçando thread acabar para prosseguir
while tf1.is_alive():
    print('Esperando Thread...')
    sleep(1.5)

print('Thread finalizada')
'''
# ------------------------------------------------------------------------------------------------------------------------------
# solucionando problema de execução com Lock()

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock() 

    def comprar(self, quantidade):
        self.lock.acquire() # "trancando entrada"

        if self.estoque < quantidade:
            print('Sem ingressos suficientes')
            self.lock.release() # "reabrindo" entrada
            return
        
        sleep(1)
        self.lock.release() # "reabrindo" entrada

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).\n'
              f'Temos {self.estoque} em estoque')


ingresso = Ingressos(10)

threads = []  # Lista para manter as threads
for i in range(1, 10):
    t = Thread(target=ingresso.comprar, args=(i,))
    threads.append(t)

# Inicia as threads
for t in threads:
    t.start()

# Verifica se todas as threads terminaram
executando = True
while executando:
    executando = False

    for t in threads:
        if t.is_alive():
            executando = True
            break

print(f'ingressos em estoque {ingresso.estoque}')
