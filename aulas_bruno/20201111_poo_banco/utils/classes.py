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
        return f"{self.nome.title()} [CPF: {self.cpf}]"
    
    # Checa se CPF já está cadastrado na base
    def __checa_cpf(self, file_path:str):
        """Checa se CPF já está cadastrado

        > Argumentos:
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
            if self.cpf in cpfs:
                return True
            else:
                return False

    # Realizar cadastro de pessoa
    def cadastrar(self, file_path:str):
        """Cadastro dos dados de uma pessoa

        > Argumentos:
            - file_path (str): Caminho para arquivo contendo dados.
        
        > Output:
            - Sem output.
        """
        if self.__checa_cpf(file_path):
            print(f"\n   > Usuário {str(self)} já cadastrado!\n")
        else:
            with open(file_path, "a") as f:
                f.write(f"{self.cpf};{self.nome}\n")
            print(f"\n   > {str(self)} cadastrado com sucesso!\n")


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

    def cadastrar(self, file_path:str):
        """Realiza cadastro do Banco

        > Argumentos:
            - file_path (str): Caminho para arquivo contendo dados.
            
        > Output:
            - Sem output.
        """
        # Recupera bancos cadastrados
        try:
            with open(file_path, "r") as f:
                bancos = f.read().splitlines()
            
        # Arquio não existe
        except FileNotFoundError:
            with open(file_path, "a") as f:
                f.write(f"{self.nome_banco}\n")
            print(f"\n   > {self.nome_banco} cadastrado com sucesso!\n")
            
        # Arquivo existe
        else:
            # Verifica se CPF já cadastrado
            if self.nome_banco in bancos:
                print(f"\n   > Banco {self.nome_banco} já cadastrado!\n")
            else:
                with open(file_path, "a") as f:
                    f.write(f"{self.nome_banco}\n")
                print(f"\n   > {self.nome_banco} cadastrado com sucesso!\n")


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
