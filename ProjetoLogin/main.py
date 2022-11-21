import mysql.connector
from biblioteca import *

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "usuarios"
)

entrada_de_comandos = banco.cursor()

while True:
    interface = int(input("Opções de acesso: "
                          "\nExibir Lista[ 1 ]    Cadastro de usuario[ 2 ]"
                          "\nSair[ 3 ] \ndigite sua escolha: "))
    if interface == 3:
        break

    elif interface == 1:
        tabela = pesquisa_banco(entrada_de_comandos)
        for x in tabela:
            print(x)
    elif interface == 2:
        usuario = input("Digite um usuario para ser adicionado ao banco: ")
        senha = input("Digite uma senha para o usuario: ")

        while True:
            if len(senha) <= 8:
                copular_banco(usuario,senha,entrada_de_comandos,banco)
                break

            else:
                print("A senha deve ter no maximo 8 caracters")
                senha = input("Digite uma senha para o usuario: ")


entrada_de_comandos.close()
banco.close()