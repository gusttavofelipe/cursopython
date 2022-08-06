from cliente import Cliente
from banco import Banco
from conta import Corrente, Poupanca

banco = Banco()

cliente1 = Cliente('Gustavo', 17)
cliente2 = Cliente('Felipe', 16)
cliente3 = Cliente('João', 23)

conta1 = Poupanca(1111, 643634, 0)
conta2 = Corrente(1111, 643631, 0)

cliente1.insere_conta(conta1)
cliente2.insere_conta(conta2)

banco.insere_cliente(cliente1)
banco.insere_conta(conta1)

banco.insere_cliente(cliente2)
banco.insere_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print()

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')