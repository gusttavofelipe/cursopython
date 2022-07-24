'''
criando excessões:

crie uma classe com o nome que deseja para a excessão e erde de "Exception"
a classe da excessão não deve ter corpo
'''

class TaErradoError(Exception): 
    pass


# tratando a excessão
def teste():
    raise TaErradoError('Algo está errado')

try:
    teste()
except TaErradoError as e:
    print(f'Erro: {e}')
    
