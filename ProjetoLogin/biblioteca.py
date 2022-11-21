def copular_banco(nome,senha,cursor,objetoBanco):
    comando_sql = "INSERT INTO cadastros (email,senha) VALUES (%s,%s);"
    dados = (nome,senha)
    executa = cursor.execute(comando_sql,dados), objetoBanco.commit()
    return executa

def pesquisa_banco(cursor):
    comando_sql = "SELECT * FROM cadastros;"
    cursor.execute(comando_sql)
    prompt = cursor.fetchall()
    return prompt