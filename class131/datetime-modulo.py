from datetime import datetime, timedelta
from time import time

# datetime(data) - formata datas (com hora, minuto, segundo etc opcionais)
data = datetime(2022, 8, 15, 19, 1, 54)
print(data)

# usando diretrizes na formatação- strftime(diretrizes)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# formatando data como str - strptime(data, format)
data2 = datetime.strptime('15/08/2022 19:01:54', '%d/%m/%Y %H:%M:%S')
print(data2)

# obtendo timestamp da data - timestamp()
print(data2.timestamp())

# usando timestamp para criar a data - fromtimestamp(timestamp)
data3 = datetime.fromtimestamp(1660600914.0)
print(data3)

data4 = datetime.strptime('15/08/2022 19:01:54', '%d/%m/%Y %H:%M:%S')

# adiciona unidades de tempo a data (suporta unidades em calculo) - timedelta(unidades)
data4 = data4 + timedelta(days=5, hours=1, minutes=1, seconds=2*60*60)
print(data4)

data5 = datetime.strptime('20/08/2022 19:01:54', '%d/%m/%Y %H:%M:%S')

data6 = datetime.strptime('15/08/2022 19:01:54', '%d/%m/%Y %H:%M:%S')

# é possivel obter a difença das datas fazendo subtração simples e
# tambem mostrar a diferença classificada por unidade de tempo 
dif = data5 - data6
print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif.days)

# mostra apenas dias horas e segundos - time()
print(data6.time(), data5.time())

# tabem é possivel fazer comparação entre as datas
print(data5 > data6)