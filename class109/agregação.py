from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa', 75)
p2 = Produto('Short', 54)
p3 = Produto('Boné', 25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produtos()
print(carrinho.soma_total())