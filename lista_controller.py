# Classe de comunicação com o banco de dados para operações com a lista

from con_db import conexao

class ClasseLista:

    def closeCon(self):
        try:
            conexao.con.close()
            print("Conexão Fechada Com Sucesso!")
        except Exception as e:
            print("Erro ao fechar a conexão\n",e)

    def inserirItens(self,itemLista):
        try:
            conexao.cur.execute('INSERT INTO Palavra (nomePalavra,significado) VALUES (?,?)',(itemLista.palavra,itemLista.significado))
        except Exception as e:
            print("Falha ao inserir o registro!\n",e)
            conexao.con.rollback()
        else:
            conexao.con.commit()
            print("Registro inserido com sucesso!")

    def listarItens(self,lim):
        try:
            result = conexao.cur.execute('SELECT * FROM Palavra LIMIT ?',(lim,)).fetchall()
        except Exception as e:
            print("Erro ao realizar a consulta!\n",e)
            return
        for line in result:
            print(line)

controller = ClasseLista()