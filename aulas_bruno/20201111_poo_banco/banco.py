"""
Programação Orientada a Objetos (POO)
    - Sistema de Cadastro Bancário

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-12

"""

# Standard Library imports
import sys

# Importando classes e funções
from utils.classes import Pessoa, Banco, Conta
from utils.numeros import ler_opcao, ler_float

# Caminhos para arquivos contendo base de dados
PESSOAS_PATH = "data/pessoas.txt"
BANCOS_PATH = "data/bancos.txt"
CONTAS_PATH = "data/contas.txt" 


def listar_clientes(file_path:str):
    """Carrega lista de clientes cadastrados

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.
    
    > Output:
        - (dict): Lista de pessoas cadastradas.
    """
    # Realiza leitura de arquivo contendo dados de clientes
    try:
        with open(file_path, "r") as f:
            clientes = [x.strip() for x in f.read().splitlines()]
    
    # Se arquivo não existir, retorna lista vazia
    except FileNotFoundError:
        return []
    
    # Retorna lista de clientes cadastrados
    else:
        return clientes


def listar_bancos(file_path:str) -> list:
    """Carrega lista de bancos cadastrados

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.
    
    > Output:
        - (dict): Lista de pessoas cadastradas.
    """
    # Realiza leitura de arquivo contendo dados de bancos
    try:
        with open(file_path, "r") as f:
            bancos = sorted(f.read().splitlines())
    
    # Se arquivo não existir, retorna lista vazia
    except FileNotFoundError:
        return []
    
    # Retorna lista de clientes cadastrados
    else:
        return bancos


def selecionar_cliente() -> Pessoa:
    """Selecionar cliente para nova conta

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (Pessoa): Objeto da classe pessoa.
    """
    # Carregar lista de clientes
    clientes = listar_clientes(PESSOAS_PATH)

    # Checa se existem clientes cadastrados
    if len(clientes) == 0:
        print("\nNenhum cliente cadastrado, realizando novo cadastro...")
        return cadastro_cliente()
    
    # Realiza seleção de cliente cadastrado
    else:
        # Apresenta opcoes do menu 
        print("\n> Selecionar Cliente:\n")
        for pos, cliente in enumerate(clientes):
            cpf, nome = cliente.split(";")
            print(f"[{pos+1}] {nome} - CPF: {cpf}")
        
        # Selecao de cliente para nova conta
        opcao = ler_opcao(clientes, "\nDigite um opção: ")
        cpf, nome = clientes[opcao-1].split(";")
        
        # Retornando objeto da classe pessoa
        return Pessoa(nome, cpf)


def selecionar_banco() -> str:
    """Selecionar banco para nova conta

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (str): Nome do banco selecionado.
    """
    # Carregar lista de pessoas
    bancos = listar_bancos(BANCOS_PATH)

    # Checa se existem clientes cadastrados
    if len(bancos) == 0:
        print("\nNenhum banco cadastrado, realizando novo cadastro...")
        return cadastro_banco()
    
    # Realiza seleção de cliente cadastrado
    else:
        # Apresenta opcoes do menu 
        print("\n> Selecionar Banco:\n")
        for pos, banco in enumerate(bancos):
            print(f"[{pos+1}] {banco}")
        
        # Selecao de cliente para nova conta
        opcao = ler_opcao(bancos, "\nDigite um opção: ")
        
        # Retornando string com nome do banco
        return bancos[opcao-1]


def cadastro_cliente() -> Pessoa:
    """Cadastro de Novo Cliente

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (Pessoa): Objeto da classe Pessoa representando o cliente.
    """
    # Cria objeto Pessoa
    print("\n" + f"{' Cadastro de Novo Cliente ':-^50}")
    p = Pessoa(
        input("\nNome: "),
        input("CPF: ")
        )
    
    # Realiza o cadastro
    p.cadastrar(PESSOAS_PATH)
    print("-"*50)

    # Retorno o objeto
    return p


def cadastro_banco() -> str:
    """Cadastro de Banco

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (str): Nome do banco cadastrado.
    """
    # Cria objeto Banco
    print("\n" + f"\n {' Cadastro de Novo Banco ':-^50}")
    b = Banco(input("\nNome do Banco: "))
    
    # Realiza o cadastro
    b.cadastrar(BANCOS_PATH)
    print("-"*50)

    # Retorno o objeto
    return b.nome_banco


def cadastro_conta():
    """Cadastro de Nova Conta Bancária

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # pass
    print("\n" + f"{' Cadastro de Nova Conta ':-^50}")
    pessoa = selecionar_cliente()
    banco = selecionar_banco()
    saldo = ler_float("\nSaldo inicial (R$): ", 0)
    # conta = Conta(banco, pessoa, saldo)
    # conta.cadastrar()


def apresentar_menu(opcoes_menu:list):
    """Apresenta Menu Principal

    > Argumentos:
        - opcoes_menu (list): Lista contendo opções do menu.
    
    > Output>
        - Sem output.
    """
    # Apresenta opcoes do menu 
    print("\n" + "=-"*25)
    print(f"\n{' SISTEMA DE CADASTRO BANCÁRIO 1.0 ':^50}\n")
    print("=-"*25)
    print("\n> Menu Principal:\n")
    for pos, opcao in enumerate(opcoes_menu):
        print(f"[{pos+1}] {opcao}")


def main():
    """Sistema para Cadastros de Bancos e Contas

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresenta menu principal
    while True:

        # Lista de opcoes do menu
        opcoes_menu = [
            "Cadastrar Cliente",
            "Cadastrar Banco",
            "Cadastrar Nova Conta",
            "Listar Clientes Cadastrados",
            "Listar Bancos Cadastrados",
            "Listar Contas Cadastradas",
            "Consultar Saldo",
            "Realizar Saque",
            "Realizar Depósito",
            "Sair do sistema",
            ]

        # Apresentar menu e captar opcao do usuario
        apresentar_menu(opcoes_menu)
        opcao = ler_opcao(opcoes_menu, "\nDigite um opção: ")

        # Cadastrar Pessoa
        if opcao == 1:
            cadastro_cliente()
              
        # Cadastrar Banco
        elif opcao == 2:
            cadastro_banco()
        
        # Cadastrar Nova Conta
        elif opcao == 3:
            cadastro_conta()
        
        # Listar Clientes Cadastrados
        elif opcao == 4:
            pass

        # Listar Bancos Cadastrados
        elif opcao == 5:
            pass
        
        # Listar Contas Cadastradas
        elif opcao == 6:
            pass
        
        # Consultar Saldo
        elif opcao == 7:
            pass
        
        # Realizar Saque
        elif opcao == 8:
            pass
        
        # Realizar Depósito
        elif opcao == 9:
            pass
        
        # Sair do sistema
        elif opcao == 10:
            sys.exit("\nSaindo, até logo!...\n")

        # Indicar opção inválida
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":

    # Executar sistema se estiver no namespace principal
    main()
    