# a hierarquia da herança funciona ordenadamente de cima para baixo.
# as subclasses não herdam nada uma da outra, apenas da classe mãe

# Super classe, classe mãe
class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classe = self.__class__.__name__

    
    def qual_classe(self):
        print(f'executando classe {self.classe}')


class Cliente(Pessoa): # herdando da classe mãe tudo que a nela, construtor, metodos atributos etc
    def comprar(self): 
        print(f'{self.classe} Esta comprando')

  
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.classe} Esta estudando')

        