'''
while/Else
contadores
acumuladores

#variavel que recebe o numero no laço while chama-se: contador
#variavel usada para acumular valores chama-se: acumulador
'''

contador = 1
acumulador = 0

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1

    if contador > 5:
        break
else:
    print('Cheguei no else')
print('Cheguei no else')

#é possivel usar else num laço de repetição
#utiliza-lo é diferente de usar apenas um comando
#fora do laço pra ser executado quando acabar
#a cadeia de comando de else será executada de acordp
#com a condição dada