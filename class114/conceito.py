# modulos para tornar classe abstrata
from abc import ABC, abstractmethod

 # uma classe abstrata não pode ser instanciada
 # obrigando as classes filhas a criarem (sobreporem) os metodos da classe abstrata em si proprias

class A(ABC):       
    @abstractmethod 
    def falar(self):
        print('falando em B')


class B(A):
    def falar(self):
        print('falando em B')

a = B()
a.falar()