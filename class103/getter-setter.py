
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, percentual): # desconta o percentual indicado do valor do produto
        self.preco = self.preco - (self.preco *(percentual / 100))
    

    # Getter: retorna o valor do atributo depois de passar pelo Setter
    @property 
    def preco(self): # o metodo criado para o "Getter"  por convenção recebe o mesmo nome do atributo copiado por ele
        return self._preco 


    # Setter: recebe o valor do atributo e faz algo antes de ser retornado pelo Getter
    @preco.setter # sempre é nomeado como: "nome do atributo copiado pelo getter+.setter" 
    def preco(self, valor): # formata preços de strings com "R$" para float  
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


    # Getter
    @property 
    def nome(self):
        return self._nome

    # Setter 
    @nome.setter # define a primeira letra do nome como maiúscula
    def nome(self, nome):
        self._nome = nome.title()


p1 = Produto('bota', 'R$100')
p1.desconto(50)
print(p1.nome, p1.preco)

p2 = Produto('Bota', 100)
p2.desconto(50)
print(p2.nome, p2.preco)
