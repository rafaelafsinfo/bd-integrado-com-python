import mysql.connector
from mysql.connector import Error


deletar = 0
while deletar not in (1, 2, 3, 4, 5):
    deletar = input("(1) para adicionar uma editora\n(2) para adicionar um(a) autor(a)\n(3) para adicinar um livro\n(4) para adicionar um cliente \n(5) para adicionar um emprestimo")
    while deletar.isnumeric() == False:
        deletar = input("digite um valor numerico para continuar")
    if deletar not in (1, 2, 3, 4, 5):
        print("opção invalida! escolha uma valida")
# fim do modulo de opção de inserção


try:
    connection = mysql.connector.connect(host='localhost', database='biblioteca', user='root', password='')
    # teste de conexão
    if connection.is_connected():
        db_Info = connection.get_server_info()
    print("Conectado ao mysql versão", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("Você está conectado: ", record)
    # inicio do modulo de deletar de dados
    cnt = "SIM"
    while cnt == "SIM" or cnt == "S":
        if deletar == 1:
            controle = "sim"
            while controle == "s" or controle == "sim":
                sql_select_Query = "select * from editora"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                record = cursor.fetchone()
                print(record)
                # Delete a record
                id = input("digite o id da editora")
                while id.isnumeric() == False:
                    id = input("digite um id valido")
                id = int(id)
                sql_Delete_query = f"""Delete from editora where id = {id}"""
                cursor.execute(sql_Delete_query)
                connection.commit()
                print('number of rows deleted', cursor.rowcount)
                controle = input("Deseja continuar deletando editoras")

        if deletar == 2:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                sql_select_Query = "select * from autor"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                record = cursor.fetchone()
                print(record)
                # Delete a record
                id = input("digite o id do autor")
                while id.isnumeric() == False:
                    id = input("digite um id valido: ")
                id = int(id)
                sql_Delete_query = f"""Delete from autor where id = {id}"""
                cursor.execute(sql_Delete_query)
                connection.commit()
                print('number of rows deleted', cursor.rowcount)
                controle = input("Deseja continuar deletando autores")
        if deletar == 3:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                sql_select_Query = "select * from livro"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                record = cursor.fetchone()
                print(record)
                # Delete a record
                id = input("insira o id do livro:")
                while id.isnumeric() == False:
                    id = input("digite um id valido:")
                id = int(id)
                sql_Delete_query = f"""Delete from livro where id = {id}"""
                cursor.execute(sql_Delete_query)
                connection.commit()
                print('number of rows deleted', cursor.rowcount)
                controle = input("Deseja continuar deletando livros")
        if deletar == 4:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                sql_select_Query = "select * from usuario"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                record = cursor.fetchone()
                print(record)
                # Delete a record
                id = input("insira o id do usuario")
                while id.isnumeric() == False:
                    id = input("digite um id valido")
                id = int(id)
                sql_Delete_query = f"""Delete from usuario where id = {id}"""
                cursor.execute(sql_Delete_query)
                connection.commit()
                print('number of rows deleted', cursor.rowcount)
                controle = input("Deseja continuar deletando usuarios")
        if deletar == 5:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                sql_select_Query = "select * from emprestimos"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                record = cursor.fetchone()
                print(record)
                # Delete a record
                id = input("insira o id do emprestimo")
                while id.isnumeric() == False:
                    id = input("digite um id valido")
                id = int(id)
                sql_Delete_query = f"""Delete from emprestimos where id = {id}"""
                cursor.execute(sql_Delete_query)
                connection.commit()
                print('number of rows deleted', cursor.rowcount)
                controle = input("Deseja continuar deletando emprestimos").upper()
        cnt = input("deseja continuar inserindo dados nas as tabelas").upper()
        if cnt == "SIM" or cnt == "S":
            deletar = 0
            while deletar not in (1, 2, 3, 4, 5):
                deletar = int(input("(1) para adicionar uma editora\n(2) para adicionar um(a) autor(a)\n(3) para adicinar um livro\n(4) para adicionar um cliente \n(5) para adicionar um emprestimo"))

                if deletar not in (1, 2, 3, 4, 5):
                    print("opção invalida! escolha uma valida")
# fim do mudulo de deletar de dados

except Error as e:
    print("Erro na conexão", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexão fechada")