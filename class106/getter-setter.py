
class Pessoa:

    def __init__(self, nome):
        self.nome = nome 
        # self._nome = nome 

    @property # toda vez que um getter ou setter é criado, o metodo passa a ser chamado como um atributo da classe
    def nome(self):
        return self._nome 
    

    @nome.setter
    def nome(self, nome):
        print('executado')
        self._nome = nome


p1 = Pessoa('Gustavo')
print(p1.nome) # usa-se o metodo sem (), pois é interpretado como atributo quando definido como getter

# getters e setters podem ter valores de diferentes
