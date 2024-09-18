import mysql.connector
from mysql.connector import Error

def conect_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='Dbescola',
            user='seu_usuario',
            password='sua_senha'
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados.")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_cidade(conexao, nome, uf):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO tbl_cidades (nome, uf) VALUES (%s, %s)"
        cursor.execute(sql, (nome, uf))
        conexao.commit()
        print("Cidade adicionada com sucesso.")
    except Error as e:
        print(f"Erro ao adicionar cidade: {e}")

def ler_cidades(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_cidades")
        resultados = cursor.fetchall()
        for cidade in resultados:
            print(cidade)
    except Error as e:
        print(f"Erro ao ler cidades: {e}")

def criar_curso(conexao, nome, valor):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO tbl_cursos (nome, valor) VALUES (%s, %s)"
        cursor.execute(sql, (nome, valor))
        conexao.commit()
        print("Curso adicionado com sucesso.")
    except Error as e:
        print(f"Erro ao adicionar curso: {e}")

def ler_cursos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_cursos")
        resultados = cursor.fetchall()
        for curso in resultados:
            print(curso)
    except Error as e:
        print(f"Erro ao ler cursos: {e}")

def criar_professor(conexao, nome, endereco, email, telefone, cpf, idade, cod_cidade):
    try:
        cursor = conexao.cursor()
        sql = """INSERT INTO tbl_professores (nome, endereco, email, telefone, cpf, idade, cod_cidade)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (nome, endereco, email, telefone, cpf, idade, cod_cidade))
        conexao.commit()
        print("Professor adicionado com sucesso.")
    except Error as e:
        print(f"Erro ao adicionar professor: {e}")

def ler_professores(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_professores")
        resultados = cursor.fetchall()
        for professor in resultados:
            print(professor)
    except Error as e:
        print(f"Erro ao ler professores: {e}")

def criar_usuario(conexao, nome, username, senha):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO tbl_usuarios (nome, username, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, username, senha))
        conexao.commit()
        print("Usuário adicionado com sucesso.")
    except Error as e:
        print(f"Erro ao adicionar usuário: {e}")

def ler_usuarios(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios")
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)
    except Error as e:
        print(f"Erro ao ler usuários: {e}")

def criar_aluno(conexao, nome, endereco, email, telefone, idade, cod_cidade, cod_curso):
    try:
        cursor = conexao.cursor()
        sql = """INSERT INTO tbl_alunos (nome, endereco, email, telefone, idade, cod_cidade, cod_curso)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (nome, endereco, email, telefone, idade, cod_cidade, cod_curso))
        conexao.commit()
        print("Aluno adicionado com sucesso.")
    except Error as e:
        print(f"Erro ao adicionar aluno: {e}")

def ler_alunos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_alunos")
        resultados = cursor.fetchall()
        for aluno in resultados:
            print(aluno)
    except Error as e:
        print(f"Erro ao ler alunos: {e}")

conexao = conect_banco()

if conexao:
    criar_cidade(conexao, 'Itumbiara', 'GO')
    ler_cidades(conexao)

    criar_curso(conexao, 'Engenharia de Software', 2000.00)
    ler_cursos(conexao)

    criar_professor(conexao, 'Carlos Roberto', 'Rua c', 'carlosm@escola.com', '123456789', '12345678998', 21, 1)
    ler_professores(conexao)

    criar_usuario(conexao, 'Bruna', 'bru123', 'senha1')
    ler_usuarios(conexao)



    conexao.close()
