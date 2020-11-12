"""
Programação Orientada a Objetos (POO)
    - Sistema de Cadastro Bancário (Classes)

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-12

"""


class Pessoa:
    """Pessoa

    > Argumentos:
        - nome (str): Nome 
        - cpf (str): CPF sem pontos nem traços
    """
    # Método construtor
    def __init__(self, nome:str, cpf:str):
        self.nome = nome.strip().title()
        self.cpf = cpf
    
    # Representação do instância na forma de string
    def __str__(self):
        """Apresenta nome e CPF

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (str): Representação da pessoa na forma de string.
        """
        return f"{self.nome} [CPF: {self.cpf}]"


class Banco:
    """Instituição Finaceira (Banco)

    > Argumentos:
        - nome_banco (str): Nome fantasia do banco.
    """
    # Método construtor
    def __init__(self, nome_banco:str):
        self.nome_banco = nome_banco.strip().upper()
    
    # Representação do instância na forma de string
    def __str__(self):
        """Apresenta nome do banco

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (str): Representação do banco na forma de string.
        """
        return self.nome_banco


class DataSaver():
    """Classe para alimentação do banco de dados
    """
    # Método Construtor
    def __init__(self):
        pass
    

    # Método para checar se cliente já está cadastrado
    def __checa_cpf(self, cpf:str, file_path:str) -> bool:
        """Checa se CPF já está cadastrado

        > Argumentos:
            - cpf (str): CPF do cliente.
            - file_path (str): Caminho para arquivo contendo dados.
        
        > Output:
            - (bool): Indicação se CPF já está cadastrado.
        """
        try:
            # Recupera CPFs cadastrados
            with open(file_path, "r") as f:
                cpfs = [x.split(";")[0] for x in f.read().splitlines()]
        
        # Arquio não existe
        except FileNotFoundError:
            return False
        
        # Arquivo existe
        else:
            # Verifica se CPF já cadastrado
            if cpf in cpfs:
                return True
            else:
                return False
    
    # Método para checar se cliente já está cadastrado
    def __checa_banco(self, nome_banco:str, file_path:str) -> bool:
        """Checa se CPF já está cadastrado

        > Argumentos:
            - nome_banco (str): Nome fantasia do banco.
            - file_path (str): Caminho para arquivo contendo dados.
        
        > Output:
            - (bool): Indicação se o banco já está cadastrado.
        """
        try:
            # Recupera CPFs cadastrados
            with open(file_path, "r") as f:
                bancos = [x for x in f.read().splitlines()]
        
        # Arquio não existe
        except FileNotFoundError:
            return False
        
        # Arquivo existe
        else:
            # Verifica se obanco já cadastrado
            if nome_banco in bancos:
                return True
            else:
                return False

    # Método para cadastrar cliente
    def cadastrar_cliente(self, obj:Pessoa, file_path:str) -> tuple:
        """Armazenar informações do cliente

        > Argumentos:
            - obj (Pessoa): Objeto da classe Pessoa;
            - file_path (str): Caminho do banco de dados.
        
        > Output:
            - (tuple):
                [0] (bool): Indicação de foi salvo ou não;
                [1] (str): Mensagem de confirmação.
        """
        # Checa cpf existe
        if not self.__checa_cpf(obj.cpf, file_path):
            # Se cliente nao cadastrado, realiza o cadastro
            with open(file_path, "a") as f:
                f.write(f"{obj.cpf};{obj.nome}\n")
            return True, "Cliente cadastrado com sucesso!"
        else:
            # Cliente já cadastrado, não realiza cadastro 
            return False, "Cliente já cadastrado!"
    
    # Método para cadastrar banco
    def cadastrar_banco(self, obj:Banco, file_path:str) -> tuple:
        """Armazenar informações do banco

        > Argumentos:
            - obj (Pessoa): Objeto da classe Banco;
            - file_path (str): Caminho do banco de dados.
        
        > Output:
            - (tuple):
                [0] (bool): Indicação de foi salvo ou não;
                [1] (str): Mensagem de confirmação.
        """
        # Checa cpf existe
        if not self.__checa_banco(obj.nome_banco, file_path):
            # Se cliente nao cadastrado, realiza o cadastro
            with open(file_path, "a") as f:
                f.write(f"{obj.nome_banco}\n")
            return True, "Banco cadastrado com sucesso!"
        else:
            # Cliente já cadastrado, não realiza cadastro 
            return False, "Banco já cadastrado!"


    
    # # Checa se CPF já está cadastrado na base
    # def __checa_cpf(self, file_path:str):
    #     """Checa se CPF já está cadastrado

    #     > Argumentos:
    #         - file_path (str): Caminho para arquivo contendo dados.
        
    #     > Output:
    #         - (bool): Indicação se CPF já está cadastrado.
    #     """
    #     try:
    #         # Recupera CPFs cadastrados
    #         with open(file_path, "r") as f:
    #             cpfs = [x.split(";")[0] for x in f.read().splitlines()]
        
    #     # Arquio não existe
    #     except FileNotFoundError:
    #         return False
        
    #     # Arquivo existe
    #     else:
    #         # Verifica se CPF já cadastrado
    #         if self.cpf in cpfs:
    #             return True
    #         else:
    #             return False

    # # Realizar cadastro de pessoa
    # def cadastrar(self, file_path:str):
    #     """Cadastro dos dados de uma pessoa

    #     > Argumentos:
    #         - file_path (str): Caminho para arquivo contendo dados.
        
    #     > Output:
    #         - Sem output.
    #     """
    #     if self.__checa_cpf(file_path):
    #         print(f"\n   > Usuário {str(self)} já cadastrado!\n")
    #     else:
    #         with open(file_path, "a") as f:
    #             f.write(f"{self.cpf};{self.nome}\n")
    #         print(f"\n   > {str(self)} cadastrado com sucesso!\n")


    # def cadastrar(self, file_path:str):
    #     """Realiza cadastro do Banco

    #     > Argumentos:
    #         - file_path (str): Caminho para arquivo contendo dados.
            
    #     > Output:
    #         - Sem output.
    #     """
    #     # Recupera bancos cadastrados
    #     try:
    #         with open(file_path, "r") as f:
    #             bancos = f.read().splitlines()
            
    #     # Arquio não existe
    #     except FileNotFoundError:
    #         with open(file_path, "a") as f:
    #             f.write(f"{self.nome_banco}\n")
    #         print(f"\n   > {self.nome_banco} cadastrado com sucesso!\n")
            
    #     # Arquivo existe
    #     else:
    #         # Verifica se CPF já cadastrado
    #         if self.nome_banco in bancos:
    #             print(f"\n   > Banco {self.nome_banco} já cadastrado!\n")
    #         else:
    #             with open(file_path, "a") as f:
    #                 f.write(f"{self.nome_banco}\n")
    #             print(f"\n   > {self.nome_banco} cadastrado com sucesso!\n")


class Conta(Banco):
    """Conta Bancária

    Classe para a representação de uma conta bancária.

    > Argumentos:
        - nome_banco (str): Instituição financeira da conta;
        - pessoa (Pessoa): Titular da conta;
        - saldo (float): Saldo da conta, em R$.
    """
    # Método construtor
    def __init__(self, nome_banco:str, pessoa:Pessoa, saldo:float):
        self.pessoa = pessoa
        self.saldo = saldo
        super().__init__(nome_banco)
    
    # Representação do instância na forma de string
    def __str__(self):
        """Apresenta informações da conta

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (str): Representação da conta na forma de string.
        """
        res = "> Conta Bancária:\n"
        res += f"   Titular: {self.pessoa.nome}\n"
        res += f"   CPF: {self.pessoa.cpf}\n"
        res += f"   Conta: {self.num_conta}\n"
        res += f"   Agência: {self.agencia}\n"
        res += f"   Banco: {self.nome_banco}\n"
        return res
    
    # Cadastro de conta
    def cadastrar():
        """Salvar dados da nova conta

        > Argumentos:
            - file_path (str): Caminho para arquivo contendo dados.
        
        > Output:
            - Sem output.
        """
        with open(file_path, "a") as f:
                f.write(f"{self.cpf};{self.nome}\n")
        print(f"\n   > {str(self)} cadastrado com sucesso!\n")
