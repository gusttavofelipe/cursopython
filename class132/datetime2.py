from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# traduz o idioma da data para o desejado.
# o segundo argumento pode ser opcionalmente uma str vazia
# que traduz para o idioma detectado na maquina
setlocale(LC_ALL, 'pt_BR.utf-8') 

# datetime.now() - obtem a data atual
dt = datetime.now() 

format = dt.strftime('%A, %d de %m %B de %Y')
print(format)

# pegando mês atual
mes_atual = int(dt.strftime('%m'))

# mdays - lista com quantidade de dias dos mêses
print(mdays[mes_atual]) # usando mês atual como indice