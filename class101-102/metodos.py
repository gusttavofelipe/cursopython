from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = f'{idade} anos'
    

    def ano_nascimento(self):
        print(self.ano_atual - self.idade)
    

    @classmethod # tornando o metodo abaixo um metodo referente propria classe (metodo de classe)
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # tornando o metodo abaixo um metodo statico. não se utiliza "self", "cls" para referenciar
                   # semelhante a uma função normal qualquer. não se tem acesso a "self" nem "cls" dentro desse metodo
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# ----------------------------------------------------------------------------------------------------------------------------------------------
# obtendo mesmo resultado com metodo e metodo de classe
p1 = Pessoa.por_ano_nascimento('Gustavo', 2005) 
p1 = Pessoa('Gustavo', 17)
print(p1.nome, p1.idade)

# metodos estaticos podem ser chamados tanto pela instancia como pela classe
print(p1.gera_id()) 
print(Pessoa.gera_id())
