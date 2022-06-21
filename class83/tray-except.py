
# try - tenta executar os codigos dentro dele
# - caso aja excessões/erros nesse codigo:
# except - é usado para tratar essas excessões/erros identificados dentro de try

a={}
try:
    try: # (segundo bloco) é possivel usar try except dentro de try except. excessões dentro desses blocos fazem com q outros blocos não sejam executados
        c = 1/0
    except ZeroDivisionError as divi:
        print('Erro:', divi)
    print(a[0]) # executado junto do segundo bloco pois esta na mesma identação
except NameError as erro1:
    print('Erro:', erro1)
except (IndexError, KeyError): # as - define a excessão como valor da variavel setada
    print('Erro de Indice ou chave')  
except Exception as excp: # Excepetion trata qualquer excessão no código, pois não a especificação - usada para erros inesperados
    print('Erro inesperado:', excp)
else: # else será executado apenas quando não houverem erros no código
    print('executado com sucesso')
finally: # finally é executado independente da existencia de erros, sempre será excutado
    b = 'Ecessão tratada' # tratando, dando valor a variavel b não definida antes

print(b) # SERIA gerada uma excessão, pois b não havia sido definido