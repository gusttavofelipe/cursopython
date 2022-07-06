
def show_add(tasks): # exbibe as tarefas 
    print()
    print('Tarefas:\n')
    for i in tarefas:
        print(i)
    print()
    

def adicionar(new, tarefas): # adiciona a nova tarefa a lista
    tarefas.append(new)


def desfazer(tarefas, suporte_tarefas): # desfaz/remove a ultima tarefa adicionada
    if not tarefas:
        print('Nada a desfazer')
        return
    ultimo = tarefas.pop()
    suporte_tarefas.append(ultimo)


def refazer(tarefas, suporte_tarefas): # refaz/readiciona a ultima tarefa removida a lista
    if not suporte_tarefas:
        print('Nada a refazer')
        return
    ultimo = suporte_tarefas.pop()
    tarefas.append(ultimo)


tarefas = []
suporte_tarefas = []

while True:
    print()
    new = input('                   Nova Tarefa\nls (listar) / df (desfazer) / rf (refazer) / x (sair):\n\n   --> ')

    if new == 'x' or new == 'X':
        break
    elif new == 'ls':
        show_add(tarefas)
        continue
    elif new == 'df':
        desfazer(tarefas, suporte_tarefas)
        continue
    elif new == 'rf':
        refazer(tarefas, suporte_tarefas)
        continue
    adicionar(new, tarefas)

    
        
