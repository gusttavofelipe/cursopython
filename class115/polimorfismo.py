'''
polimorfismo de sobreposição:
é um principio que permite que classes derivadas de uma mesma superclasse
tenham metodos iguais (de mesma assinatura) mas comportamentos diferentes.
mesma assinatura = mesma quantidade e tipo de parametros
'''

from abc import ABC, abstractmethod # superclasse

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg): # modificando metodo da superclasse
        print(f'B esta falando sobre {msg}')


class C(A): # modificando metodo da superclasse
    def fala(self, msg):
        print(f'C esta falando sobre {msg}')


b = B()
b.fala('carros')

a = C()
a.fala('futebol')