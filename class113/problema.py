
class A:
    def falar(self):
        print('falando em A')


class B(A):
    def falar(self):
        print('falando em B')


class C(A):
    def falar(self):
        print('falando em C')


class D(B, C):
    pass


d = D()
d.falar()

# problema do diamante

# o valor é buscado da esquerda para direita na cadeia da herança, caso não seja encontrado
# na ultima classe da cadeia, o valor é buscado na classe pela qual foi passada a herança