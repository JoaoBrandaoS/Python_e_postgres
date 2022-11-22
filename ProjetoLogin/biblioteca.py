
class BancoDeDados():
    def __init__(self,cliente = False,senha = False,database= False
                 ,cursorDeEntrada = False):
        self.cliente = cliente
        self.senha = senha
        self.database = database
        self.cursorDeEntrada = cursorDeEntrada

    def interface(self):
        return int(input("Opções de acesso: "
                              "\nExibir Lista[ 1 ]    Cadastro de usuario[ 2 ]"
                              "\nSair[ 3 ] \ndigite sua escolha: "))

    def copularBanco(self,nome,senha,cursor,banco):
        comando_sql = "INSERT INTO cadastros (email,senha) VALUES (%s,%s);"
        dados = (nome,senha)
        executa = cursor.execute(comando_sql,dados), banco.commit()
        return executa

    def pesquisarNaTabela(self,cursor):
        comando_sql = "SELECT * FROM cadastros;"
        cursor.execute(comando_sql)
        prompt = cursor.fetchall()
        return prompt