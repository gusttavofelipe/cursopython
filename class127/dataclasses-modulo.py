'''
O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário, que tambem podem ser dsativados.
'''

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

            
@dataclass(eq=True, order=True, repr=True, frozen=False, init=True)
class Pessoa: 
   nome: str
   sobrenome: str = field(repr=False) # desativando/omitindo a variavel sobrenome do "repr"

   @property
   def nome_completo(self):
      return f'{self.nome} {self.sobrenome} '


p1 = Pessoa('B', 'Felipe')
p2 = Pessoa('C', 'Felipe')
p3 = Pessoa('D', 'Felipe')
p4 = Pessoa('A', 'Felipe')
p5 = Pessoa('A', 'Felipe')

print(p4 == p5) # usando igualdade com parametro "eq"

pessoas = [p1, p2, p3, p4]
print(sorted(pessoas)) # usando sorted com parametro "order"

print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)  

# fazendo casts do objeto 
print(astuple(p1)) # tupla
print(asdict(p1)) # dict