
from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Gustavo')
caneta = Caneta('Faber Castle')
maquina = MaquinaDeEscrever()

# associando classes: atribuindo o objeto "caneta" inteiro a "ferramenta"
# chamada de associação fraca
escritor.ferramenta = caneta 
escritor.ferramenta.escrever()

# 
