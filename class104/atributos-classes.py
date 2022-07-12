
class A:
    vc = 123

a1 = A()
a2 = A()
A.vc = 321 # muda o valor do atributo da classe, pois foi alterado pela classe
a1.vc = 123 # CRIA um valor direto na instancia, não modifica o valor atribuido na classe

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print()

print(a1.vc)
print(a2.vc)
print(A.vc)

print(f'{220*"-"}\n')

# o valor do atributo é buscado primeiramente na propria instancia,
# se lá não houver, é buscado na classe e atribuido 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

class B:
    gu = 456

    def __init__(self):
        self.gu = 654

b1 = B()
b2 = B()
b1.vc = 456

print(b1.__dict__)
print(b2.__dict__)
print(B.__dict__)

print()

print(b1.gu)
print(b2.gu)
print(B.gu)

# no caso de haver atributos de metodos, classe e ainda atribuir o valor do atributo diretamente
# na instancia tendo esses o mesmo nome, a prioridade é do atributo do metodo