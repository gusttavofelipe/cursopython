# agregação: uma classe usa outra como parte de si e necessita dela para funcionar corretamente

class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []
    

    def inserir_produto(self, produto): # insere produtos na lista
        self.produtos.append(produto)


    def lista_produtos(self): # exibe os produtos da lista
        for produto in self.produtos:
            print(produto.nome, produto.valor)


    def soma_total(self): # exibe o valor da soma total dos produtos
        total = 0
        for produto in self.produtos:
            total += produto.valor 
        return total


class Produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor