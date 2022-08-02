# metaclasses: são classes que criam outras classes/(definem o comportamento)

class Meta(type): # metaclasse

    def __new__(mcs, name, bases, namespace): 
        print(mcs) # informações da metaclasse
        print(name) # nome da classe
        print(bases) # herança da classe
        print(namespace) # informções sobre as classes

        if name == 'A':  
            return type.__new__(mcs, name, bases, namespace)
                
        if 'sobrescrever' in namespace: # impedindo que atributos herdados sejam sobrescritos
            print(f'{name} tentou sobrescrever o atributo ')
            del namespace['sobrescrever']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    sobrescrever = 'valor A'

class B(A):
    sobrescrever = 'valor B'


b = B()
print(b.sobrescrever)