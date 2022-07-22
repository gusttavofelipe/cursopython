from conta import Conta


class contaPoupanca(Conta):
    def sacar(self, valor): # saca um valor da conta
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
        