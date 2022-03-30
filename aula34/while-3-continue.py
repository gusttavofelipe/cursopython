

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # continue faz com que as linhas de código após ele não sejam executadas e volte ao laço de repetição
    print(x)
    x = x + 1

print('Acabou!')