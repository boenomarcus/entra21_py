"""
Introdução - SQLite
    - Alterando campos da tabela

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

# Cria colunas para ajustar tabela ao novo padrão
cursor.execute("""
ALTER TABLE carros
    ADD COLUMN nome TEXT;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN num_portas INTEGER;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN km_rodado REAL;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN qtd_passageiros INTEGER;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN motor TEXT;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN combustivel TEXT;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN meio_locomocao TEXT;
""")

cursor.execute("""
ALTER TABLE carros
    ADD COLUMN valor REAL;
""")

# Cria commit das alterações
conn.commit()

# Indica que novas colunas foram criadas
print('Novos campos adicionados com sucesso.')

# Fecha conexão com a base de dados
conn.close()    
