from datetime import datetime

class Pessoa: # classe Pessoa
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) # variaveis da classe em si podem ser usada tando pelas instancias como pela propria classe 
    def __init__(self, nome, idade, comendo=False, falando=False): # os valores enviados na instancia serão atribuidos aos paramtros do metodo 
        self.nome = nome  # atribuindo os parametros do metodo como valores das variaveis
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        # "self" referencia algo a propria instancia
        
    def comer(self, alimento): # faz a pessoa comer
        if self.comendo:  
            print(f'{self.nome} ja está comendo.')
            return
        
        if self.falando:
            print('pare de falar para comer ')
            return

        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):  # faz a pessoa parar decomer
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False
    

    def falar(self, assunto):   # faz a pessoa falar 
        if self.comendo:
            print(f'{self.nome} não pode falar de boca cheia.')
            return
        
        if self.falando:
            print(f'{self.nome} ja tá na resenha.')
            return

        print(f'{self.nome} esta falando sobre {assunto} ')
        self.falando = True


    def para_falar(self):   # faz a pessoa parar de falar
        if not self.falando:
            print(f'{self.nome} não está conversando.')
            return

        print(f'{self.nome} parou de conversar.')
        self.falando = False


    def ano_nascimento(self):   # imprime o ano de nascimento da pessoa
        print(self.ano_atual - self.idade)
        return 