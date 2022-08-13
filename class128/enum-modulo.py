from enum import Enum, auto
'''
sempre que haver um conjunto de opcoes, valores a escolher
Enum é mais recomendavel a se usar (do que um if, por exemplo).
'''

class Direcoes(Enum):
    esquerda = auto() # auto() enumera automaticamente o valor
    direita = auto()
    cima = auto()
    baixo = auto()
    

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Não é possível mover para essa direção')

    return f'mover para {direcao.name}'


if __name__ == '__main__':
    print(mover(Direcoes.direita))
    print(mover(Direcoes.esquerda))
    print(mover(Direcoes.cima))
    print(mover(Direcoes.baixo))

    print()

    for direcao in Direcoes:
        print(f'{direcao} {direcao.value} - {direcao.name}')

