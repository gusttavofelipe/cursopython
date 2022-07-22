from conta import Conta


class contaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite


    @property
    def limite(self):
        return self._limite


    def sacar(self, valor): # saca um valor da conta
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()