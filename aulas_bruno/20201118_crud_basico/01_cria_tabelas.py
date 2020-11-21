"""
Sistema CRUD Básico: Clientes e Veículos
    - Criação de tabelas no SQLite

Blusoft/Senac - Formação em Python Entra21 2020

Autores:
    - Leonardo da Silva Kostetzer
    - Marcus Moresco Boeno
    - Thiago Augusto Zeferino

Último Update: 2020-11-21

"""

# Importando 
import sqlite3

# Cria conexão com banco de dados
conn = sqlite3.connect('clientes.db')

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

try:
    # Criando a tabela de clientes
    cursor.execute("""
    CREATE TABLE clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento DATE NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        salario REAL NOT NULL,
        profissao TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        nome_de_responsavel TEXT,
        sexo TEXT NOT NULL,
        naturalidade TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
    );
    """)
    
    # Criando a tabela de veiculos
    cursor.execute("""
    CREATE TABLE veiculos (
        id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano VARCHAR(4) NOT NULL,
        placa VARCHAR(8) NOT NULL,
        num_portas INTEGER NOT NULL,
        cor TEXT NOT NULL,
        km_rodado REAL NOT NULL,
        qtd_passageiros INTEGER NOT NULL,
        motor INTEGER NOT NULL,
        combustivel TEXT NOT NULL,
        meio_locomocao TEXT NOT NULL,
        valor REAL NOT NULL,
        id_cliente INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
    );
    """)
    
    # Indica criação da tabela
    print('Tabela criada com sucesso.')

    # Realiza commit das mudanças realizadas
    conn.commit()

    # Fechando a conexão
    conn.close()

except:
    print("Tabela já criada.")
