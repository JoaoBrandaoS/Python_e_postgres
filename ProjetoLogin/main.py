import psycopg2
from biblioteca import *

#======================================================================================================
#   Ligação com o banco de dados., neste projeto foi utilizad o o postgres
#======================================================================================================
banco = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "postgres",
    database = "postgres"
)
#======================================================================================================
#ja neste bloco crio todas os objetos necessarios para acesar as classes da como o proprio cursor para
#trazer dados do banco ou dar commit para o proprio
#======================================================================================================

entrada_de_comandos = banco.cursor()
funcao = BancoDeDados()
objetos = BancoDeDados()

#=======================================================================================================
#aqui criamos um While infinito para servir como interface no prompt
while True:
    interface = funcao.interface() #ja aqui chamamos a função interface para criar um ambiente de opções.
    if interface == 3:
        break #neste if caso a opção escolhida seja 3 logo o bloco de codigos é encerrado

    elif interface == 1:
        #ja nesta opção chamo a função pesquisarNaTabela para imprimir todas os dados da tabela contida dentro
        #do banco

        objetos.cursorDeEntrada = entrada_de_comandos
        tabela = funcao.pesquisarNaTabela(objetos.cursorDeEntrada)
        for x in tabela:
            print(x)

    elif interface == 2:
        #ja aqui solicito um login do usuario para que ele tenha permição para efetuar copulação do banco
        login = input("Digite o login de Adm: ")
        senha = input("Digite a senha de Adm: ")
        objetos.cursorDeEntrada = entrada_de_comandos
        verificaLogin = funcao.logarNoBanco(objetos.cursorDeEntrada,login,senha)

        if len(verificaLogin) != 0:
            objetos.admin = True
            #aqui é feito uma verificação para saber se o dado digitado pelo usuario é igual ao dado ja
            #aceito no banco

            if objetos.admin == True:
                #aqui é  feito a copulação do banco de dados.

                objetos.cliente = input("Digite um usuario para ser adicionado ao banco: ")
                objetos.senha = input("Digite uma senha para o usuario: ")
                objetos.cursorDeEntrada = entrada_de_comandos
                objetos.database = banco
                while True:

                    #aqui refaço uma verificação para que tenhamos garantia que a senha adicionada terá ate 8
                    #caracteres
                    if len(objetos.senha) <= 8:
                        funcao.copularBanco(objetos.cliente,objetos.senha,
                                        objetos.cursorDeEntrada,objetos.database)
                        break #caso tudo esteja certo o novo usuario é adicionado

                    else:
                            print("A senha deve ter no maximo 8 caracters")
                            objetos.senha = input("Digite uma senha para o usuario: ")
            else:

                print("Você não tem acesso a função de copular o banco de dados.")

#======================================================================================================
entrada_de_comandos.close()
banco.close()
#ja aqui fechamos a conexão com o banco de dados e também o cursor criado para evitar criação de varias
#pontes com o banco de dados que iriam ficar abertas
#======================================================================================================