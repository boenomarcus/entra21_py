import sqlite3

# Cria conexão com banco de dados
conn = sqlite3.connect('20201118_crud_basico/clientes.db')

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

try:
    # Criando a tabela de veiculos
    cursor.execute("""
    CREATE TABLE carros (
            id_carro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano VARCHAR(4) NOT NULL,
            cor TEXT NOT NULL,
            placa VARCHAR(8) NOT NULL,
            proprietario TEXT NOT NULL,
            num_portas INTEGER NOT NULL,
            km_rodado REAL NOT NULL,
            qtd_passageiros INTEGER NOT NULL,
            motor TEXT NOT NULL,
            combustivel TEXT NOT NULL,
            meio_locomocao TEXT NOT NULL,
            valor REAL NOT NULL
    );
    """)

    # Criando a tabela de pessoas
    cursor.execute("""
    CREATE TABLE pessoas (
            id_pessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data_nascimnto DATE NOT NULL,
            cpf TEXT NOT NULL,
            endereco TEXT NOT NULL,
            salario REAL NOT NULL,
            profissao TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            nome_de_responsavel TEXT NOT NULL,
            sexo TEXT NOT NULL,
            naturalidade TEXT NOT NULL,
            nacionalidade TEXT NOT NULL
    );
    """)

    # Indica criação da tabela
    print('Tabela criada com sucesso.')

    # Fechando a conexão
    conn.close()
except:
    print("Tabela já criada")
