
import sqlite3

# Os módulos do python funcionam como um objeto singleton.
# Um módulo é chamado uma única vez, logo a var conexao é instanciada uma unica vez na memoria

class DataBaseCon:

    def __init__(self):
        try:
            #Supondo que o palavrasIngles.db já esteja no mesmo diretório desse módulo
            self.con = sqlite3.connect('palavrasIngles.db')
            self.cur = self.con.cursor()
            print("Conexão Realizada!")
        except Exception as e:
            print("Erro ao conectar na base de dados\n",e)

conexao = DataBaseCon()
