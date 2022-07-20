  
class Pessoa: 
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade
        self.classe = self.__class__.__name__


    def falar(self):
        print(f'{self.classe} esta falando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.classe} esta estudando.')


class Cliente(Pessoa): 
    def comprar(self): 
        print(f'{self.classe} esta comprando.')


    def falar(self):
        print(f'{self.classe} esta em Cliente...')

  
class ClienteVIP(Cliente): # herdando de "Cliente" que herdou de "Pessoa"

    def __init__(self, idade, nome, sobrenome): # sobrepondo construtor de "Pessoa". adicionando "sobrenome"
        Pessoa.__init__(self, idade, nome) # referenciando que o construtor de "Pessoa" será sobreposto
        # super().__init__(nome, idade) 
        self.sobrenome = sobrenome

    def falar(self): # sobrepondo metodo da classe "Cliente"
        # super().falar() 
        Pessoa.falar(self) # chamando metodo da classe "Pessoa" antes de ser sobreposto
        Cliente.falar(self) # chamando metodo da classe "Cliente" antes de ser sobreposto
        print(f'{self.nome} {self.sobrenome} está falando.') 



# deve-se passar os parametros de metodo e construtor que deseja chamar, referenciar ou executar antes 
# super() faz referencia ou chama UM metodo, construtor ou classe ANTERIOR AO ATUAL


