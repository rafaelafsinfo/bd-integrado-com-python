import mysql.connector
from mysql.connector import Error


adicionar = 0
while adicionar not in (1, 2, 3, 4, 5):
    adicionar = input("(1) para adicionar uma editora\n(2) para adicionar um(a) autor(a)\n(3) para adicinar um livro\n(4) para adicionar um cliente \n(5) para adicionar um emprestimo")
    while adicionar.isnumeric() == False:
        adicionar = input("digite um valor numérico para continuar")
    adicionar= int(adicionar)
    if adicionar not in (1, 2, 3, 4, 5):
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
        if adicionar == 1:
            controle = "sim"
            while controle == "s" or controle == "sim":
                id_editora = input("insira o id da editora")
                while id_editora.isnumeric() == False:
                    id_editora = input("insira um id valido")
                id_editora = int(id_editora)
                nome_editora = input("insira o nome da editora")
                mySql_insert_query = f"""INSERT INTO editora (id,nome) VALUES ({id_editora}, '{nome_editora}') """
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Editora inserida com sucesso")
                cursor.close()
                controle = input("Deseja continuar adicionando editoras")

        if adicionar == 2:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id_autor = input("insira o id do autor")
                while id_autor.isnumeric() == False:
                    id_autor = input("insira um ID valido")
                id_autor = int(id_autor)
                nome_autor = input("insira o nome do autor")
                mySql_insert_query = f"""INSERT INTO autor (id,nome) VALUES ({id_autor}, '{nome_autor}') """
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Autor inserido com sucesso")
                cursor.close()
                controle = input("Deseja continuar adicionando autores").upper()
        if adicionar == 3:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id_livro = input("insira o id do livro")
                while id_livro.isnumeric() == False:
                    id_autor = input("insira um ID valido")
                id_livro = int(id_livro)
                id_autor = input("insira o id do autor")
                while id_autor.isnumeric() == False:
                    id_autor = input("insira um ID valido")
                id_autor = int(id_autor)
                id_editora = input("insira o id da editora")
                while id_editora.isnumeric() == False:
                    id_editora = input("insira um ID valido")
                id_editora = int(id_editora)

                titulo_livro = input("insira o titulo do livro")

                ano = input("insira o ANO de publicação")
                while ano.isnumeric() == False:
                    ano = input("insira um ANO valido")
                ano = int(ano)

                isbn = input("insira o ISBN do livro")
                while isbn.isnumeric() == False:
                    isbn= input("insira um ISBN valido")
                isbn = int(isbn)

                mySql_insert_query = f"""INSERT INTO livros (id,titulo,autor_id,editora_id,ano_publicacao,isbn) VALUES ({id_livro},'{titulo_livro}',{id_autor},{id_editora},{ano},{isbn}) """
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Livros inserido com sucesso")
                cursor.close()
                controle = input("Deseja continuar adicionando livros").upper()
        if adicionar == 4:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id_usuario = input("insira o id do usuario")
                while id_usuario.isnumeric() == False:
                    id_usuario = input("insira um ID valido")
                id_usuario = int(id_usuario)
                nome_usuario = input("insira o nome do usuario")
                endereco = input("insira o endereço do usuario")
                telefone = input("insira o telefone do usuario")
                while telefone.isnumeric() == False:
                    telefone = input("insira um ID valido")
                telefone = int(telefone)
                email = input("insira o email do usuario")

                mySql_insert_query = f"""INSERT INTO usuario (id,nome,endereco,telefone,email) VALUES ({id_usuario},'{nome_usuario}','{endereco}',{telefone},'{email}') """
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "Usuario inserido com sucesso")
                cursor.close()
                controle = input("Deseja continuar adicionando usuarios").upper()
        if adicionar == 5:
            controle = "SIM"
            while controle == "S" or controle == "SIM":
                id_emprestimo = input("insira o id do emprestimo")
                while id_emprestimo.isnumeric() == False:
                    id_emprestimo = input("insira um ID valido")
                id_emprestimo = int(id_emprestimo)
                id_usuario = input("insira o id do usuario")
                while id_usuario.isnumeric() == False:
                    id_usuario = input("insira um ID valido")
                id_usuario = int(id_usuario)
                id_livro = input("insira o id do livro")
                while id_livro.isnumeric() == False:
                    id_livro = input("insira um ID valido")
                id_livro = int(id_livro)
                data_emprestimo = input("insira a data do emprestimo no modelo americano (ano-dia-mes)")
                data_devolucao = input("insira a data de devolução no modelo americano (ano-dia-mes)")

                mySql_insert_query = f"INSERT INTO emprestimos(id, usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES ({id_emprestimo},{id_usuario},{id_livro},'{data_emprestimo}','{data_devolucao}')"
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                print(cursor.rowcount, "emprestimo inserido com sucesso")
                cursor.close()
                controle = input("Deseja continuar adicionando emprestimos").upper()
        cnt = input("deseja continuar inserindo dados nas as tabelas").upper()
        if cnt == "SIM" or cnt == "S":
            adicionar = 0
            while adicionar not in (1, 2, 3, 4, 5):
                adicionar = int(input("(1) para adicionar uma editora\n(2) para adicionar um(a) autor(a)\n(3) para adicinar um livro\n(4) para adicionar um cliente \n(5) para adicionar um emprestimo"))

                if adicionar not in (1, 2, 3, 4, 5):
                    print("opção invalida! escolha uma valida")
# fim do mudulo de injeção de dados

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexão fechada")
