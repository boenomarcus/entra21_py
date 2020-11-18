"""
Introdução - SQLite
    - Criando nova tabela

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último Update: 2020-11-18

"""
# Carrega DB-API
import sqlite3

# Cria conexão com banco de dados
conn = sqlite3.connect('20201117_sqlite3_intro/carros.db')

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

# Criando a tabela no banco de dados
cursor.execute("""
CREATE TABLE pessoas (
        id_pessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data_nascimento DATE NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        salario REAL NOT NULL,
        profissao TEXT NOT NULL
);
""")

# Indica criação da tabela
print('Tabela criada com sucesso.')

# Fechando a conexão
conn.close()
