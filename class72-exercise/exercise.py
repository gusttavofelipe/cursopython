
carrinho = []
carrinho.append(('produto1', 43))
carrinho.append(('produto2', 54.50))
carrinho.append(('produto1', 23.45))
    
total = sum([float(y) for x, y in carrinho])
print(f'Valor total dos pedidos: R${total}')