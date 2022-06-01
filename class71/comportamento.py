'''
Quando o numero de prints excede o numero de iterações do iteravel, é levantada uma StopIteration indicando o "esgotamento"/fim das iterações. Usando "try" o comportamento muda e passa a ser semelhante ao do "for", não exbindo nada além do valor da iteração e não apresentando StopIteration após exceder o numero "máximo de iterações"
'''

nome = 'Gustavo Felipe'
iterador = iter(nome)
gerador = (letra for letra in nome)

try:
    print(next(iterador)) #G
    print(next(iterador)) #u
    print(next(iterador)) #s
    print(next(iterador)) #t
    print(next(iterador)) #a
    print(next(iterador)) #v
    print(next(iterador)) #o
    print(next(iterador)) #
    print(next(iterador)) #f
    print(next(iterador)) #e
    print(next(iterador)) #l
    print(next(iterador)) #i
    print(next(iterador)) #p
    print(next(iterador)) #e
    print(next(iterador)) 
except:
    pass

print('>>>>>>>For<<<<<<<')
for i in iterador:  # após todas as iterações forem "consumidas", ao utilizar o for, nada mais será exibido
    print(i)
print('-'*90)
try:
    print(next(gerador)) #G
    print(next(gerador)) #u
    print(next(gerador)) #s
    print(next(gerador)) #t
    print(next(gerador)) #a
    print(next(gerador)) #v
    print(next(gerador)) #o
    print(next(gerador)) #
    print(next(gerador)) #f
    print(next(gerador)) #e
    print(next(gerador)) #l
    print(next(gerador)) #i
    print(next(gerador)) #p
    print(next(gerador)) #e
    print(next(iterador)) 
except:
    pass

print('>>>>>>>For<<<<<<<')
for j in gerador:  # identicamente a um iterador, um gerador, após todas as iterações forem "consumidas", ao utilizar o for nada mais será exibido
    print(j)