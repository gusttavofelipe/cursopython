from corrente import contaCorrente
from conta import Conta
from poupanca import contaPoupanca


print('Poupança:')
print()

poupanca = contaPoupanca(4932, 345, 0)
poupanca.depositar(100)
poupanca.sacar(50)
poupanca.sacar(50)
poupanca.sacar(50)

print()
print('Conta corrente:')
print()

corrente = contaCorrente(6544, 344, 0, 100)
corrente.depositar(100)
corrente.sacar(50)
corrente.sacar(50)
corrente.sacar(50)
corrente.sacar(50)
corrente.sacar(50)
corrente.depositar(1000)


# impssivel instanciar classe 
# c = Conta(4932, 345, 0)
# c.depositar(100)