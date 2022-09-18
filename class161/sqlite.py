import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

# estabelecendo conexão com a base de dados
conexao = sqlite3.connect(f'{BASE_DIR}/class161/basededados.db')
cursor = conexao.cursor() # executa os comando sql na base de dados

# criando tabela caso não exista
# "clientes" - nome da tabela
# dentro dos parenteses - colunas
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,' # INTEGER = int, AUTOINCREMENT - incrementa +1 no id
                'nome TXT,' # TXT = str
                'peso REAL' # REAL = float
                ')')

# INSERT INTO - inserindo em clientes, nos campos/colunas nome e peso
# VALUES - valores ordenadamente nos campos/colunas
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Gustavo Felipe', 54.9))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Gustavo', 'peso':75})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Felipe', 'peso':63})
# conexao.commit() # executa os comandos

#  modificando dados 
cursor.execute('UPDATE clientes SET nome = :nome WHERE id = :id', {'nome': 'Gustavo Fring', 'id': 2})
conexao.commit() 

#  deletando todos os dados de um id
cursor.execute('DELETE FROM clientes WHERE id = :id', {'id': 3})
conexao.commit() 

 # cursor.execute('SELECT * FROM clientes') # mostra tudo que esta em clientes

# # mostrando dados usando condicionais
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 60})

for linha in cursor.fetchall():
    nome, peso = linha 
    print(nome, peso)


cursor.close()
conexao.close()