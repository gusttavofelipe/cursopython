import sqlite3
import os 

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        # OR IGNORE - ignora o dado/não adiciona se o mesmo valor ja estiver na base
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id): 
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id): 
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conexao.commit()    

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            idd, nome, telefone = linha
            print(idd, nome, telefone)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome like ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        # % no inico e fim indicam a busca do valor em qualquer posicão
        # tanto no inicio como no meio ou fim

        for linha in self.cursor.fetchall():
            idd, nome, telefone = linha
            print(idd, nome, telefone)

    def fechar(self):   
        self.cursor.close()
        self.conexao.close()


if __name__ == '__main__':
    agenda = AgendaDB(f'{BASE_DIR}/class164/agenda.db')
    agenda.buscar('Peterson')
   