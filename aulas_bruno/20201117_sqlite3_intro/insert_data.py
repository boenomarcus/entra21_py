"""
Introdução - SQLite
    - Inserindo novos dados

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último Update: 2020-11-18

"""
# Carrega DB-API
import sqlite3
    
# Cria conexão com banco de dados
conn = sqlite3.connect("20201117_sqlite3_intro/carros.db")

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

# Declara objetos
carros = [
    ("Renault", "Sandero", "2015", "Prata", "SHJ-2061", "João da Silva"),
    ("Peugeot", "2008", "2019", "Bordô", "JIA-2008","Pedro Paulo Vasconcellos")
    ]
    
# Insere objetos no DB
cursor.executemany(
    """
    INSERT INTO carros (marca, modelo, ano, cor, placa, proprietario)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    carros
    )

# Cria commit das alterações
conn.commit()

# Indica que dados foram inseridos no DB
print('Registros adicionados ao banco de dados.')

# Fecha conexão com a base de dados
conn.close()

