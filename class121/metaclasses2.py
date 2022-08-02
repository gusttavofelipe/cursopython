
class Meta(type): # metaclasse
    def __new__(mcs, name, bases, namespace): 
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'b_fala' not in namespace:
            print(f'crie o metodo "b_fala" em {name}')
        else:
            if not callable(namespace['b_fala']):
                print('b_fala deve ser um metodo')

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta): # indicando a metaclasse
    def fala(self):
        self.b_fala()
        
    
class B(A):
    b_fala = 'falando'
    def b_fala(self):
        print('oi')

b = B()