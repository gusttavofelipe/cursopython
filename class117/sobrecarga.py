
'''
Sobrecarga de operadores: altera o comportamento
de um operador por meio de um metodo especial.
'''

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self. y = y

    def get_area(self): # área do retangulo
        return self.x * self.y


    def __repr__(self):
        return f'<class "Retangulo({self.x}, {self.y})"' 


    def __add__(self, other): # alterando operador (+)
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    

    def __lt__(self, other): # alterando operador (<)  
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else: 
            return False

    def __gt__(self, other): # alterando operador (>)
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else: 
            return False


    def __eq__(self, other): # alterando operador (==)
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1+r2
# print(r3)
print(r2 == r3)

