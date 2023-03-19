import mysql.connector
from mysql.connector import Error

selecao = 0
while selecao not in (1, 2, 3, 4, 5):
    selecao = int(input("(1) para analisar a tabela de editoras\n(2) para analisar a tabela de autores\n(3) para analisar a tabela de livros\n(4) para analisar a tabela de clientes\n(5) para analisar a tabela de emprestimos"))
    if selecao not in (1, 2, 3, 4, 5):
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
    # inicio do modulo de injeção de dados
    cnt = "SIM"
    while cnt == "SIM" or cnt == "S":
        # editora
        if selecao == 1:
            controle = "sim"
            while controle == "s" or controle == "sim":
                id = int(input("insira o id da editora"))
                sql_select_Query = f"select * from editora where id = '{id}';"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total de registros: ", cursor.rowcount)
                print("\nPrinting cada linha")
                for row in records:
                    print("id = ", row[0], )
                    print("nome = ", row[1], "\n")
                controle = input("Deseja analisando editoras").upper()
        # autor
        if selecao == 2:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id = int(input("insira o id do autor"))
                sql_select_Query = f"select * from autor where id = '{id}';"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total de registros: ", cursor.rowcount)
                print("\nPrinting cada linha")
                for row in records:
                    print("id = ", row[0], )
                    print("nome = ", row[1], "\n")
                controle = input("Deseja analisando autores").upper()
        # autor
        if selecao == 3:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id = int(input("insira o id do livro"))
                sql_select_Query = f"select * from livros where id = '{id}';"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total de registros: ", cursor.rowcount)
                print("\nPrinting cada linha")
                for row in records:
                    print("id = ", row[0], )
                    print("titulo = ", row[1], "\n")
                    print("autor_id = ", row[2], "\n")
                    print("editora_id = ", row[3], "\n")
                    print("ano = ", row[4], "\n")
                    print("isbn = ", row[5], "\n")
                controle = input("Deseja analisando livros").upper()
        # usuario
        if selecao == 4:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id = int(input("insira o id do usuario"))
                sql_select_Query = f"select * from usuario where id = '{id}';"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total de registros: ", cursor.rowcount)
                print("\nPrinting cada linha")
                for row in records:
                    print("id = ", row[0], )
                    print("nome = ", row[1], "\n")
                    print("endereço = ", row[2], "\n")
                    print("telefone = ", row[3], "\n")
                    print("email = ", row[4], "\n")

                controle = input("Deseja analisando usuarios").upper()
        # emprestimo
        if selecao == 5:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id = int(input("insira o id do emprestimo"))
                sql_select_Query = f"select * from emprestimos where id = '{id}';"
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                # get all records
                records = cursor.fetchall()
                print("Total de registros: ", cursor.rowcount)
                print("\nPrinting cada linha")
                for row in records:
                    print("id = ", row[0], )
                    print("id do usuario = ", row[1], "\n")
                    print("id do livro = ", row[2], "\n")
                    print("emprestimo = ", row[3], "\n")
                    print("devolucao = ", row[4], "\n")

                controle = input("Deseja analisando emprestimos").upper()
        cnt = input("deseja continuar inserindo dados nas as tabelas").upper()
        if cnt == "SIM" or cnt == "S":
            selecao = 0
            while selecao not in (1, 2, 3, 4, 5):
                selecao = int(input("(1) para analisar a tabela de editoras\n(2) para analisar a tabela de autores\n(3) para analisar a tabela de livros\n(4) para analisar a tabela de clientes\n(5) para analisar a tabela de emprestimos"))
                if selecao not in (1, 2, 3, 4, 5):
                    print("opção invalida! escolha uma valida")
# fim do mudulo de injeção de dados

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexão fechada")