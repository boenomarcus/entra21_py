"""
Sistema CRUD Básico: Clientes e Veículos
    - Definição de classes

Blusoft/Senac - Formação em Python Entra21 2020

Autores:
    - Leonardo da Silva Kostetzer
    - Marcus Moresco Boeno
    - Thiago Augusto Zeferino

Último Update: 2020-11-21

"""

# Standard Library imports
import sqlite3


class Cliente:
    """Definição de classe para Clientes

    > Parâmetros de Classe:
        - nome (str): Nome completo do cliente;
        - data_nascimento (str): Data de nascimento (ISO: aaaammdd);
        - cpf (str): Cadastro de Pessoa Física (CPF);
        - endereco (str): Endereço do cliente;
        - salario (float): Salário do cliente, em R$;
        - profissao (str): Profissão do cliente;
        - email (str): Endereço eletrônico;
        - telefone (str): Número de Telefone, com DDD;
        - nome_de_responsavel (str): Nome completo do responsável,
            quando cliente for menor de idade;
        - sexo (str): Sexo do cliente (Masculino ou Feminino);
        - naturalidade (str): Cidade natal do cliente;
        - nacionalidade (str): Nacionalidade do cliente.
    """
    # Método construtor
    def __init__(self, nome:str, data_nascimento:str, cpf:str, endereco:str, 
    salario:float, profissao:str, email:str, telefone:str, 
    nome_de_responsavel:str, sexo:str, naturalidade:str, nacionalidade:str):
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
    """Definição de classe para Veículos

    > Parâmetros de Classe:
        - nome (str): Nome do veículo;
        - marca (str): Nome da montadora;
        - modelo (str): Modelo do veículo;
        - ano (str): Ano do veículo (montagem);
        - placa (str): Placa do veículo, no padrão brasileiro;
        - num_portas (int): Número de portas do veículo;
        - cor (str): Cor da lataria do veículo;
        - km_rodado (float): Quilômetros rodados pelo veículo, assim
            indicado pelo odômetro;
        - qtd_passageiros (int): Quantidade máxima de passageiros;
        - motor (int): Potência do motor, em Cavalo-Vapor (CV);
        - combustivel (str): Combustivel utilizado pelo veículo;
        - meio_locomocao (str): Força motriz do veículo;
        - valor (float): Valor do veículo, em R$;
        - id_cliente (int): ID do proprietário do veículo.
    """
    def __init__(self, nome:str, marca:str, modelo:str, ano:str, placa:str, 
    num_portas:int, cor:str, km_rodado:float, qtd_passageiros:int, motor:int,
    combustivel:str, meio_locomocao:str, valor:float, id_cliente:int):
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
    """Classe para leitura dos dados presentes na base (SQLite)

    > Parâmetros de Classe:
        - db_path (str): Caminho para arquivo (.db) contendo dados;
        - tabela (str): Nome da tabela presente no banco de dados.
    """
    # Método construtor
    def __init__(self, db_path:str, tabela:str):
        self.db_path = db_path
        self.tabela = tabela
    
    # Retorna registros contidos no banco de dados
    def retrieve_all(self) -> list:
        """Retorna todos os registros da tabela

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (list): Lista de tuplas contendo os registros do banco de
                dados. Cada registro será representado por uma tupla.
        """
        # Cria conexão para leitura de dados
        with sqlite3.connect(self.db_path) as conn:

            # Cria um cursor para interarção com o DB
            c = conn.cursor()

            # Constroi e executa comanndo SQL para leitura de dados
            c.execute(f"SELECT * FROM {self.tabela}".replace("'", ""))
            
            # Recupera dados na forma de uma lista de tuplas
            content = c.fetchall()
        
        # Retorna dados do DB
        return content


class DataWriter:
    """Classe para escrever, atualizar e deletar dados da base (SQLite)

    > Parâmetros de Classe:
        - db_path (str): Caminho para arquivo (.db) contendo dados;
        - tabela (str): Nome da tabela presente no banco de dados.    
    """
    # Método construtor
    def __init__(self, db_path:str, tabela:str):
        self.db_path = db_path
        self.tabela = tabela 
    
    # Realiza novo cadastro no banco de dados
    def insert(self, obj):
        """Realiza novo cadastro na base de dados

        > Argumentos:
            - obj (...): Objeto da classe Cliente ou Veiculo.
        
        > Output:
            - Sem output.
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
            print("\nNovo registro realizado com sucesso!\n")

        else:
            # Retorna nome da classe do objeto 
            tipo = type(obj).__name__
            print(f"Não é possível inserir objetos '{tipo}' na base de dados!")

    def update_info(self):
        """Realiza update de um cadastro de cliente ou veículo

        > Argumentos:
            - Sem argumentos
        
        > Output:
            - Sem output
        """
        # Update de informações de um cliente
        if self.tabela == "clientes":
            self.__update_info_clientes()
        
        # Update de informações de um veículo
        elif self.tabela == "veiculos":
            self.__update_info_veiculos()
        
        # Indica que tabela não existe
        else:
            raise NotImplementedError(f"Tabela '{self.tabela}'' inexistente!")    

    def __apresentar_info_cliente(self, id_cliente:int):
        """Apresenta informações do cliente em tela

        > Argumentos:
            - id_cliente (int): ID da pessoa a ser apresentada.

        > Output:
            - Sem output.
        """
        # Cria conexao, recupera infos do cliente e fecha conexao
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM clientes
            WHERE id_cliente = ?
        """, (id_cliente,))
        info_usuarios = cursor.fetchone()
        
        # Apresenta informações do usuário
        asteriscos = "*" *60
        print("\n" + asteriscos)
        print(f"{f'Informações cliente - {info_usuarios[0]}':^60}")
        print(asteriscos)
        print(f"""
        1)Nome - {info_usuarios[1]}
        2)Data de nascimento -{info_usuarios[2]}
        3)Cpf -{info_usuarios[3]}
        4)Endereço -{info_usuarios[4]}
        5)Salário -{info_usuarios[5]}
        6)Profissão -{info_usuarios[6]}
        7)E-mail -{info_usuarios[7]}
        8)Telefone -{info_usuarios[8]}
        9)Nome do Responsavél -{info_usuarios[9]}
        10)Sexo -{info_usuarios[10]}
        11)Naturalidade -{info_usuarios[11]}
        12)Nacionalidade -{info_usuarios[12]}
        """)
    
    def ___checa_id(self, id_name:str, id_usuario:int) -> bool:
        """Checa se ID indicado existe

        > Argumentos:
            - id_name (str): Nome do ID na tabela;
            - id_usuario (int): ID indicado pelo usuario.
        
        > Output:
            - (bool): Booleano indicando se ID existe ou não
        """
        with sqlite3.connect(self.db_path) as conn:
            # Cria cursor
            cursor = conn.cursor()
            
            # Executa comando SQL e recupera ids de cliente
            cursor.execute(f"SELECT {id_name} FROM {self.tabela}")
            ids = [x[0] for x in cursor.fetchall()]
        
        # Testa se ID indicado existe na base
        if id_usuario in ids:
            return True
        else:
            return False
    
    def __leitura_id(self, id_name:str):
        """Recebe ID indicado pelo usuário

        > Argumentos:
            - id_name (str): Nome do ID na tabela.
        
        > Output:
            - (int): ID indicado pelo usuário
        """
        # Leitura do ID a ser modificado
        while True:
            try:
                # Capta ID a ter registro alterado
                id_usuario = int(input("        Digite ID (0 para sair): "))
            
            # Usuário interrompeu sistema
            except KeyboardInterrupt:
                sys.exit("\n        Saindo, até logo! ...\n")
            
            # Input inválida, não é um numero inteiro
            except ValueError:
                print("        ID inválido, digite novamente!")
            
            # Checa domínio e existência de ID
            else:
                if id_usuario == 0 or self.___checa_id(id_name, id_usuario):
                    return id_usuario
                    break
                print(f"        ID ({id_usuario}) inexistente, digite novamente!")

    def __update_info_clientes(self):
        """Realiza update de informações de um cliente.

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - Sem output.
        """
        # Leitura do ID do usuário a ser modificado
        id_usuario = self.__leitura_id("id_cliente")
        
        # Se ID indicado for 0, sai da função
        if id_usuario != 0:
                    
            # Dicionário com opções disponíveis para alteração
            opcoes = {
                "1": "nome", "2": "data_nascimento", "3": "cpf", "4": "endereco",
                "5": "salario", "6": "profissao", "7": "email", "8": "telefone",
                "9": "nome_de_responsavel", "10": "sexo", "11": "naturalidade",
                "12": "nacionalidade"
                }
            
            while True:
                # Apresenta informações do cliente
                self.__apresentar_info_cliente(id_usuario) 
                
                # Capta informação a ser alterada
                while True:
                    escolha = input('Digite o numero da informação que você deseja modificar: ')
                    if escolha in opcoes.keys():
                        break
                    print("Opção inválida, digite novamente!")
                novo_elemento = input(f"Digite a alteração ({opcoes[escolha]}): ")

                # Cria comando SQL na forma de uma string
                # Exemplo de como a deve ficar:
                # """
                # UPDATE clientes SET email = 'joao_silva@gmail.com' WHERE id_cliente = 2
                # """"
                string_base = "UPDATE clientes SET "            
                string_base += f"{opcoes[escolha]}"
                string_base += f" = '{novo_elemento}'"
                string_base += f" WHERE id_cliente = {id_usuario}"
                
                # Cria conexao, executa comando e finaliza conexao
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute(string_base)
                conn.commit()
                conn.close()

                # Indica que o registro foi alterado com sucesso
                print("\n        Alterado com sucesso ...\n")
                
                # Verifca se usuario deseja fazer nova modificação
                while True:
                    continuar = input("Deseja modificar outro campo? [(s)/n]: ").strip().lower()
                    if continuar in "sn":
                        break
                    print("Opcão inválida, digite 's' ou 'n'")
                if continuar == "n":
                    break
    
    def __apresentar_info_veiculo(self, id_veiculo:int):
        """Apresenta informações do veículo em tela

        > Argumentos:
            - id_veiculo (int): ID do veículo a ser apresentada.

        > Output:
            - Sem output.
        """
        # Cria conexao, recupera infos do cliente e fecha conexao
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM veiculos
            WHERE id_veiculo = ?
        """, (id_veiculo,))
        info_veiculo = cursor.fetchone()
        
        # Apresenta informações do usuário
        asteriscos = "*" *60
        print("\n" + asteriscos)
        print(f"{f'Informações veículo - {info_veiculo[0]}':^60}")
        print(asteriscos)
        print(f"""
        1)Nome - {info_veiculo[1]}
        2)Marca -{info_veiculo[2]}
        3)Modelo -{info_veiculo[3]}
        4)Ano -{info_veiculo[4]}
        5)Placa -{info_veiculo[5]}
        6)Número de Portas -{info_veiculo[6]}
        7)Cor -{info_veiculo[7]}
        8)Quilometragem -{info_veiculo[8]}
        9)Máximo de Passageiros -{info_veiculo[9]}
        10)Motor (Potência - CV) -{info_veiculo[10]}
        11)Tipo de Combustível -{info_veiculo[11]}
        12)Força Motriz -{info_veiculo[12]}
        13)Valor -{info_veiculo[13]}
        14)ID Cliente -{info_veiculo[14]}
        """)
    
    def __update_info_veiculos(self):
        """Realiza update de informações de um veículo.

        > Argumentos:
            -  Sem argumentos.
        
        > Output:
            - Sem output.
        """
        
        # Recupera lista de clientes cadastrados na base
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
        
        # Checa se lista de clientes está vazia
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado!")
        
        else:
            # Recupera lista de veiculos
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM veiculos")
                veiculos = cursor.fetchall()

            # Checa se cliente indicado possui veiculo cadastrado ou nao
            if len(veiculos) == 0:
                print(f"Nenhum veículo cadastrado!")
            else:
                # Lista veiculos e capta id do veiculo a ser alterado
                # Apresenta lista de clientes
                print("\n" + "-"*60)
                print(f"{'VEÍCULOS CADASTRADOS':^60}")
                print("-"*60 + "\n")
                for veiculo in veiculos:
                    print(
                        "  > [ID: {}] {}-{} (Placa: {})".format(
                            veiculo[0], veiculo[1], veiculo[2], veiculo[5]
                            )
                        )
                print("\n" + "-"*60 + "\n")

                # Leitura do ID do usuário a ser modificado
                id_veiculo = self.__leitura_id("id_veiculo")

                # Loop para alteração de informações do veiculo
                # Se ID indicado for 0, sai da função
                if id_veiculo != 0:
                            
                    # Dicionário com opções disponíveis para alteração
                    opcoes = {
                        "1": "nome", "2": "marca", "3": "modelo", "4": "ano",
                        "5": "placa", "6": "num_portas", "7": "cor", 
                        "8": "km_rodado", "9": "qtd_passageiros", "10": "motor",
                        "11": "combustivel", "12": "meio_locomocao", 
                        "13": "valor", "14": "id_cliente"
                        }
                    
                    while True:
                        # Apresenta informações do cliente
                        self.__apresentar_info_veiculo(id_veiculo) 
                        
                        # Capta informação a ser alterada
                        while True:
                            escolha = input('Digite o numero da informação que você deseja modificar: ')
                            if escolha in opcoes.keys():
                                break
                            print("Opção inválida, digite novamente!")
                        novo_elemento = input(f"Digite a alteração ({opcoes[escolha]}): ")

                        # Cria comando SQL na forma de uma string
                        # Exemplo de como a deve ficar:
                        # """
                        # UPDATE clientes SET email = 'joao_silva@gmail.com' WHERE id_cliente = 2
                        # """"
                        string_base = "UPDATE veiculos SET "            
                        string_base += f"{opcoes[escolha]}"
                        string_base += f" = '{novo_elemento}'"
                        string_base += f" WHERE id_veiculo = {id_veiculo}"
                        
                        # Cria conexao, executa comando e finaliza conexao
                        conn = sqlite3.connect(self.db_path)
                        cursor = conn.cursor()
                        cursor.execute(string_base)
                        conn.commit()
                        conn.close()

                        # Indica que o registro foi alterado com sucesso
                        print("\n        Alterado com sucesso ...\n")
                        
                        # Verifca se usuario deseja fazer nova modificação
                        while True:
                            continuar = input("Deseja modificar outro campo? [(s)/n]: ").strip().lower()
                            if continuar in "sn":
                                break
                            print("Opcão inválida, digite 's' ou 'n'")
                        if continuar == "n":
                            break
    
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
        97, "Gasolina", "Combustão", 25560.46, 1
        )
    v02 = Veiculo(
        "Monza", "VW", "234-gf", "1984", "KLD-2313", 5, "Chumbo", 25600, 5, 
        55, "Gasolina", "Combustão", 25560.46, 1
        )
    v03 = Veiculo(
        "Jaguar", "Jaguar", "234-gf", "1984", "OLS-2313", 5, "Chumbo", 25600, 5,
        100, "Gasolina", "Combustão", 25560.46, 2
        )

    # Cria objeto clientes_writer e insere dados na tabela de clientes
    clientes_writer = DataWriter(DB_PATH, "clientes")
    clientes_writer.insert(c01)
    clientes_writer.insert(c02)

    # Cria objeto clientes_writer e insere dados na tabela de veiculos
    veiculos_writer = DataWriter(DB_PATH, "veiculos")
    veiculos_writer.insert(v02)
    veiculos_writer.insert(v03)

    # Recupera informações de clientes e veiculos e os apresenta em tela
    print(DataReader(DB_PATH, "clientes").retrieve_all())
    print(DataReader(DB_PATH, "veiculos").retrieve_all())
    