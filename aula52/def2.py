

def valor(funcao):
    return funcao                   # 'return' seguido da variavel, retorna o valor "real" do argumento inserido na variavel.
                                    # tudo q vem abaixo de return, não é levado em conta, return marca o fim.

var = valor('valor que eu quero')   # o valor 'none' retornado na função quando NÃO utilizado 'return' indica que: 
                                     # o dado/argumento apresentado não possui nenhum tipo de valor
if var:
    print(var)
else:
    print('nenhum valor')

# -----------------------------------------------------------

def divisao(n1, n2):
    if n2 == 0:       # divisões por zero resultam em erro, para isso, uma solução é checar antes, desse modo, é possivel inserir dois returns na mesma função
        return
    return n1 / n2    # pode-se tambem retornar a variavel executando alguma ação

divide = divisao(10, 10)
if divide:
    print(divide)
else:
    print('conta inválida')