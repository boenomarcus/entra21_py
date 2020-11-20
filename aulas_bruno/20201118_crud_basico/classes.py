
# Standard Library imports
import sqlite3


class Cliente:
    """Classe para criar clientes
    """
    def __init__(self, nome, data_nascimento, cpf, endereco, salario, 
    profissao, email, telefone, nome_de_responsavel, sexo, naturalidade, 
    nacionalidade):
        self.nome = nome
        self.data_nascimento = data_nascimento 
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_de_responsavel = nome_de_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade


class Veiculo:
    """Classe para criar veiculos
    """
    def __init__(self, nome, marca, modelo, ano, placa, num_portas, cor, 
    km_rodado, qtd_passageiros, motor, combustivel, meio_locomocao, valor, 
    id_cliente):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.num_portas = num_portas
        self.cor = cor
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        self.valor = valor
        self.id_cliente = id_cliente


class DataReader:
    """Realiza leitura dos dados presentes na base (SQLite)
    """
    def __init__(self, db_path, tabela):
        self.db_path = db_path
        self.tabela = tabela
    
    def retrieve_all(self):
        """Retorno todos os dados de uma tabela
        """
        # Cria conexão para leitura de dados no banco
        with sqlite3.connect(self.db_path) as conn:

            # Cria um cursor para interarção com o DB
            c = conn.cursor()

            # Constroi e executa comnando SQL para leitura de dados
            c.execute(f"SELECT * FROM {self.tabela}".replace("'", ""))
            
            # Recupera dados na forma de uma lista de tuplas
            content = c.fetchall()
        
        # Retorna dados do DB
        return content


class DataWriter:
    """Realiza write, update e delete na base (SQLite)
    """
    # Constructor
    def __init__(self, db_path, tabela):
        self.db_path = db_path
        self.tabela = tabela 
        
    def insert(self, obj):
        """Método para inserir dados na 
        """
        # Checa se o objeto entregue é da classe Cliente ou Veiculo
        if isinstance(obj, Cliente) or isinstance(obj, Veiculo):

            # Cria conexão para inserir dados no banco
            with sqlite3.connect(self.db_path) as conn:

                # Recupera atributos do objeto como dicionario
                data = obj.__dict__

                # Cria um cursor para interarção com o DB
                c = conn.cursor()
                
                # Constroi o comnando SQL para inserção dos dados
                query = "INSERT INTO {} {}".format(
                    self.tabela, tuple(data.keys())
                    )
                query += f" VALUES {('?',)*len(data)}"
                
                # Executa comando e gera commit para a base
                c.execute(query.replace("'", ""), tuple(data.values()))
                conn.commit()
            
            # Indica que dados foram registrados na DB
            print("Novo registro realizado com sucesso!")

        else:
            print(f"Impossível inserir objeto {type(obj).__name__} no DB")         

    def update_info(self, db_path):
        pass

    def delete_data(self, db_path):
        pass

if __name__ == "__main__":

    # Caminho para base de dados
    DB_PATH = "clientes.db"
    
    # Cria instancias da classe Cliente
    c01 = Cliente(
        "Peter", "19951008", "21798372", "rua blabla", 3500, "analista", 
        "peter@gmail.com", "1232132", None, "Masculino", "São Paulo", 
        "Brasileiro"
        )
    c02 = Cliente(
        "Carlos", "3423", "4234234", "rua hehehe", 2570.45, "Padeiro", 
        "carlos@outlook.com", "423234", "Roberta", "Masculino", "Bluemau", 
        "Brasileiro"
        )

    # Cria instancias da classe Veiculo
    v01 = Veiculo(
        "Passat", "VW", "234-gf", "1984", "HJK-2313", 5, "Chumbo",  25600, 5, 
        "1.6", "Gasolina", "kk", 25560.46, 1
        )
    v02 = Veiculo(
        "Monza", "VW", "234-gf", "1984", "KLD-2313", 5, "Chumbo", 25600, 5, 
        "1.6", "Gasolina", "kk", 25560.46, 1
        )
    v03 = Veiculo(
        "Jaguar", "Jaguar", "234-gf", "1984", "OLS-2313", 5, "Chumbo", 25600, 5,
        "1.6", "Gasolina", "kk", 25560.46, 2
        )

    # Cria objeto clientes_writer e insere dados na tabela de clientes
    clientes_writer = DataWriter(DB_PATH, "clientes")
    clientes_writer.insert(c01)
    clientes_writer.insert(c02)

    # Cria objeto clientes_writer e insere dados na tabela de veiculos
    veiculos_writer = DataWriter(DB_PATH, "veiculos")
    veiculos_writer.insert(v01)
    veiculos_writer.insert(v02)
    veiculos_writer.insert(v03)

    # Recupera informações de clientes e veiculos e os apresenta em tela
    print(DataReader(DB_PATH, "clientes").retrieve_all())
    print(DataReader(DB_PATH, "veiculos").retrieve_all())
    