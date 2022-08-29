from string import Template
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

with open(f'{BASE_DIR}/class140/template.html', 'r') as html:
    template = Template(html.read()) # lendo o arquivo html
    data_atual = datetime.now().strftime('%d/%m/%Y')
    
    # editando variaveis do html
    corpo_msg = template.substitute(nome='Gustavo', data=data_atual) 

print(corpo_msg)