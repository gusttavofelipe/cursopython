from classes import Cliente

cliente1 = Cliente('Gustavo', 17)
cliente1.insere_endereco('Santa inês', 'MA')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Felipe', 16)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Rio Branco', 'AC')
print(cliente2.nome)
cliente2.lista_endereco()
print()

cliente3 = Cliente('Maria', 36)
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
cliente3.insere_endereco('Salvador', 'BA')
print(cliente3.nome)
cliente3.lista_endereco()

