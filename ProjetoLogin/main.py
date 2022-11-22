import psycopg2
from biblioteca import *

banco = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "postgres",
    database = "postgres"
)

entrada_de_comandos = banco.cursor()
funcao = BancoDeDados()
objetos = BancoDeDados()

while True:
    interface = funcao.interface()
    if interface == 3:
        break

    elif interface == 1:
        objetos.cursorDeEntrada = entrada_de_comandos
        tabela = funcao.pesquisarNaTabela(objetos.cursorDeEntrada)
        for x in tabela:
            print(x)

    elif interface == 2:
        objetos.cliente = input("Digite um usuario para ser adicionado ao banco: ")
        objetos.senha = input("Digite uma senha para o usuario: ")
        objetos.cursorDeEntrada = entrada_de_comandos
        objetos.database = banco

        while True:
            if len(objetos.senha) <= 8:
                funcao.copularBanco(objetos.cliente,objetos.senha,
                                    objetos.cursorDeEntrada,objetos.database)
                break

            else:
                print("A senha deve ter no maximo 8 caracters")
                objetos.senha = input("Digite uma senha para o usuario: ")


entrada_de_comandos.close()
banco.close()