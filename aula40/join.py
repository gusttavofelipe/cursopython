# dividindo str com split e formando lista
string = 'O Brasil é penta'
lista = string.split(' ')

# juntando str com .join()
string2 = ' '.join(lista) 

'''
o valor da variavel foi definida como str (um espaço), esse espaço foi usado como caractere/parametro de junção para para a variavel definida 
dentro da função. Caso o q estivesse na função fosse uma str, a função iria usar o espaço como caractere/parametro para separar OS CARACTERES
dessa str
'''

print(string)
print(lista)
print(string2)