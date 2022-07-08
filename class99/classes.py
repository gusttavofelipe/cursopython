from pessoa import Pessoa

p1 = Pessoa('Gustavo', 16)
p2 = Pessoa('Felipe', 17)

# os objetos são independentes um do outro

p1.falar('Programação')
p2.comer('Torta')

p1.ano_nascimento()
p2.ano_nascimento()