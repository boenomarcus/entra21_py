"""
Introdução - SQLite

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último Update: 2020-11-17

"""
# Carrega DB-API
import sqlite3

# Cria conexão com banco de dados
conn = sqlite3.connect('carros.db')

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

# Criando a tabela no banco de dados
cursor.execute("""
CREATE TABLE carros (
        id_carro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano VARCHAR(4) NOT NULL,
        cor TEXT NOT NULL,
        placa VARCHAR(7) NOT NULL,
        proprietario TEXT NOT NULL
);
""")

# Indica criação da tabela
print('Tabela criada com sucesso.')

# Fechando a conexão
conn.close()