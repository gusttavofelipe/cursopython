'''
   sem nenhuma sinalização - (publico)
 _ recomenda-se que não seja acessado - (protected (but) public)
 __recomenda-se fortemente que não seja acessado - (private)
   as regras se aplicam a qualquer coisa que desejeda
'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {} # atributo principal (privado)

    @property # pode-se dar acesso apenas aos dados do atributo retornando o valor com um Getter
    def dados(self):
        return self.__dados


    def inserir_client(self, id, nome): # insere um nome cliente ao "banco de dados"
        if 'clients' not in self.__dados:
            self.__dados['clients'] = {id: nome}
        else:
            self.__dados['clients'].update({id: nome})


    def list_clients(self):
        for id, nome in self.__dados['clients'].items():
            print(id, nome)


    def dell_client(self, id):
        del self.__dados['clients'][id]


bd = BaseDeDados()
bd.inserir_client(1, 'Gustavo')
bd.inserir_client(2, 'Felipe')
bd.inserir_client(3, 'Costa')

bd.list_clients()
bd.__dados = 'outra coisa' # __ faz com que seja criado outro atributo de mesmo nome com o valor passado 
print(bd.__dados)  
print(bd._BaseDeDados__dados) # para acessar o valor real do atributo privado usa-se: instancia + _ + classe + atributo

print(bd.dados) # valor retornado do Getter