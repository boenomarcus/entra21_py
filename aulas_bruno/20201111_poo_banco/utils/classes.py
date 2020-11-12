"""
Programação Orientada a Objetos (POO)
    - Sistema de Cadastro Bancário (Classes)

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-11

"""

class Pessoa:
    """Pessoa

    > Argumentos:
        - nome (str): Nome 
        - cpf (str): CPF sem pontos nem traços
    """
    # Método construtor
    def __init__(self, nome:str, idade:int, cpf:str):
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


class Banco:
    """Instituição Finaceira (Banco)

    > Argumentos:
        - nome_banco (str): Nome fantasia do banco.
    """
    # Método construtor
    def __init__(self, nome_banco:str):
        self.nome_banco = nome_banco
    
    # Representação do instância na forma de string
    def __str__(self):
        """Apresenta nome do banco

        > Argumentos:
            - Sem argumentos.
        
        > Output:
            - (str): Representação do banco na forma de string.
        """
        return self.nome_banco


class Conta:
    """Conta Bancária

    Classe para a representação de uma conta bancária.

    > Argumentos:
        - banco (Banco): Instituição financeira da conta;
        - pessoa (Pessoa): Titular da conta;
        - saldo (float): Saldo da conta, em R$.
    """
    # Método construtor
    def __init__(self, banco:Banco, pessoa:Pessoa, saldo:float):
        self.banco = banco
        self.pessoa = pessoa
        self.saldo = saldo
    

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
        res += f"   Banco: {self.banco.nome_banco}\n"
        return res
