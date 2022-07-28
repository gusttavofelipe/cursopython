# alguns metodos magicos abaixo

class A:
    def __new__(cls):
        print('Método  __new__ < construtor >')
        return super().__new__(cls)


    def __init__(self):
        print('Método __init__  < inicializador >')

a = A()


class B:
    def __call__(self, *args, **kwds): # faz o objeto se comportar como uma função quando é chamado
        resul = 1                      
        for i in args:
            resul *= i
        return  f'a multiplicação de todos os números é: {resul}'
    

    def __str__(self): # retorna uma representação de string de um objeto
        return 'é minha classe'


    def __len__(self): # modifica a função "len"
        return 100


# __call__
b = B()
var = b(1,23,376,4,53)
print(var)


# __str__
d = B()
print('Esta '+str(d))


# __len__
e = B()
print(len(e))