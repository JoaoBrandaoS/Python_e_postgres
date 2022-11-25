
class BancoDeDados():
    #aqui crio uma classe para trabalhar a POO e as funções do projeto
    def __init__(self,cliente = False,senha = False,database= False
                 ,cursorDeEntrada = False,administrar = False,ComandoSql = False):
        self.cliente = cliente
        self.senha = senha
        self.database = database
        self.cursorDeEntrada = cursorDeEntrada
        self.ComandoSql = ComandoSql
        self.administrar = administrar


    def interface(self):
        return int(input("Opções de acesso: "
                              "\nExibir Lista[ 1 ]    Cadastro de usuario[ 2 ]"
                              "\nSair[ 3 ] \ndigite sua escolha: "))



    def pesquisarNaTabela(self,cursor):
        comando_sql = "SELECT * FROM cadastros WHERE ip > 1;"
        cursor.execute(comando_sql)
        self.ComandoSql = cursor.fetchall()
        return self.ComandoSql

    def copularBanco(self, nome, senha, cursor, banco):
        comando_sql = "INSERT INTO cadastros (email,senha) VALUES (%s,%s);"
        dados = (nome, senha)
        executa = cursor.execute(comando_sql, dados), banco.commit()
        return executa

    def logarNoBanco(self,cursor,nome,senha):
        comando_sql = "SELECT email, senha FROM cadastros WHERE email ='{}' AND senha = '{}'".format(nome,senha)
        cursor.execute(comando_sql)
        self.ComandoSql = cursor.fetchall()
        return self.ComandoSql