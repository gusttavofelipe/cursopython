from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia


    @property
    def conta(self):
        return self._conta

    
    @property
    def saldo(self):
        return self._saldo

    
    @saldo.setter
    def saldo(self, valor): # checa o tipo do valor de "saldo" 
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor deve ser um valor numerico')
        self._saldo = valor
    

    def depositar(self, valor): # deposita um valor na conta
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do deposito deve ser numerico')
        self._saldo += valor
        self.detalhes()
    
    
    def detalhes(self): #exibe os dados da conta
        print(f'Agencia: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}')
        print(f'Saldo: {self._saldo}')


    @abstractmethod
    def sacar(self, valor): # metodo abstrato sobreposto em "poupança" e "corrente"
        pass
