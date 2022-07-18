# composição: quando uma classe pertence a outra, é instanciada dentro da outra classe

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self. enderecos = []
    

    def insere_endereco(self, cidade, estado): # insere endereços na lista
        self.enderecos.append(Endereco(cidade, estado)) # instanciando "Endereco" com os valores do metodo
    

    def lista_endereco(self): # lista os ebdereços de cada objeto 
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado