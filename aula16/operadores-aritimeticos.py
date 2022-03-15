'''
operadores aritimeticos
+ faz adição (obviamente)
- faz subrtração (obviamente)
* faz multiplicação
/ faz divisão com ponto flutuante onde: se o resultado for um numero de ponto flutuante, será exibido com ponto flutuante
// faz divisão inteira onde: se o resultado for um numero de ponto flutuante, será exibido um valor arrendondado desse numero
** faz exponenciação
% Módulo: Retorna o resto da divisão de ambos operandos.
() altera a precedencia da operação
'''


# adição
print(10 + 10)
print('10' + '10') # somando str faz se a ação de concatenação (junção de valores).

# subtração
print(10 - 10)

# multiplicação
print(10 * 10)
print(10 * 'G')  # pode-se fazer multiplicações de strings (apenas com int). nesse caso "*" agiria como repetidor

# divisão com ponto flutuante
print(10 / 10)  # valor sempre será dado com ponto flutuante

# divisão inteira (resultado sempre arredondado para um numero int)
print(10 // 10)
print(10.8 // 10)  #na divisão inteira:se o numero que dividido for float o resultado será um numero float 'arrendondao'

# exponenciação
print(10 ** 10)

#  modulo (resto da divisão)
print(10.5 % 10)

# alteração de precedencia
print(5+2*10)
print((5+2)*10)  # altera a precedencia/ordem como na matematica normal







