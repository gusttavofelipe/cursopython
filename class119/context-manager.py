# gerenciador de contexto usando classe
 
class Abrir:
    def __init__(self, arquivo, modo): # abrindo arquivo
        self.arquivo = open(arquivo, modo)
    
    def __enter__(self): # retornando arquivo
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb): # fechando arquivo
        arquivo.close()

with Abrir('arquivo.txt', 'a+') as arquivo:
    arquivo.write('outra coisa\n')

#----------------------------------------------------------------------------------------------------------------------------------------------
# gerenciador de contexto usando função

from contextlib import contextmanager

@contextmanager # torna a função um gerenciador de contexto
def abrir(arquivo,modo):
    try:
        arquivo = open(arquivo, modo) # abrindo arquivo
        yield arquivo
    finally:
        arquivo.close() # fechando arquivo

with abrir('arquivo2.txt', 'a+') as arquivo2:
    arquivo2.write('linha 1\n')
    
