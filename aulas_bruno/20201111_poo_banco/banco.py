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
from utils.classes import Pessoa, Banco, Conta, DataSaver
from utils.numeros import ler_opcao, ler_float

# Caminhos para arquivos contendo base de dados
PESSOAS_PATH = "data/pessoas.txt"
BANCOS_PATH = "data/bancos.txt"
CONTAS_PATH = "data/contas.txt" 


def listar_registros(file_path:str) -> list:
    """Carrega lista de bancos cadastrados

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.
    
    > Output:
        - (dict): Lista de registros de clientes, bancos ou contas.
    """
    # Realiza leitura de arquivo contendo dados de bancos
    try:
        with open(file_path, "r") as f:
            bancos = f.read().splitlines()
    
    # Se arquivo não existir, retorna lista vazia
    except FileNotFoundError:
        return []
    
    # Retorna lista de clientes cadastrados
    else:
        return bancos


def selecionar_cliente(file_path:str) -> Pessoa:
    """Selecionar cliente para nova conta

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.

    > Output:
        - (Pessoa): Objeto da classe pessoa.
    """
    while True:
        # Carregar lista de clientes
        clientes = listar_registros(file_path)

        # Checa se existem clientes cadastrados
        if len(clientes) == 0:
            print("\nNenhum cliente cadastrado, realizando novo cadastro...")
            res = cadastro_cliente()
            print(res[1])
            print("-"*50)
        
        # Realiza seleção de cliente cadastrado
        else:
            # Apresenta opcoes do menu 
            print("\n> Selecionar Cliente:\n")
            print("[0] Conta com Novo Cliente")
            for pos, cliente in enumerate(clientes):
                cpf, nome = cliente.split(";")
                print(f"[{pos+1}] {nome} - CPF: {cpf}")
                        
            # Selecao de cliente para nova conta
            opcao = ler_opcao(0, len(clientes), "\nDigite um opção: ")
            
            # Checa se usuario quer cadastrar conta com novo cliente
            if opcao == 0:
                while True:
                    # Realiza novo cadastro
                    res = cadastro_cliente()

                    # Checa se cadastro ocorreu
                    if res[0]:
                        cpf, nome = listar_registros(file_path)[-1].split(";")
                        print("\n" + res[1])
                        print("Cliente selecionado para conta!")
                        break
                    
                    # Indica se cadastro não ocorreu
                    else:
                        print("CPF já cadastrado, tente novamente!")
            
            # Cadastra conta com cliente existente
            else:
                cpf, nome = clientes[opcao-1].split(";")
            
            # Retornando objeto da classe pessoa
            return Pessoa(nome, cpf)


def selecionar_banco(file_path:str) -> Banco:
    """Selecionar banco para nova conta

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.

    > Output:
        - (Banco): Objeto da classe banco.
    """
    while True:
        # Carregar lista de clientes
        bancos = listar_registros(file_path)
        
        # Checa se existem clientes cadastrados
        if len(bancos) == 0:
            print("\nNenhum banco cadastrado, realizando novo cadastro...")
            res = cadastro_banco()
            print(res[1])
            print("-"*50)
        
        # Realiza seleção de cliente cadastrado
        else:
            # Apresenta opcoes do menu 
            print("\n> Selecionar Banco:\n")
            print("[0] Conta em Novo Banco")
            for pos, banco in enumerate(bancos):
                print(f"[{pos+1}] {banco}")
                        
            # Selecao de cliente para nova conta
            opcao = ler_opcao(0, len(bancos), "\nDigite um opção: ")
            
            # Checa se usuario quer cadastrar conta com novo cliente
            if opcao == 0:
                while True:
                    # Realiza novo cadastro
                    res = cadastro_banco()

                    # Checa se cadastro ocorreu
                    if res[0]:
                        banco = listar_registros(file_path)[-1]
                        print("\n" + res[1])
                        print("Banco selecionado para conta!")
                        break
                    
                    # Indica se cadastro não ocorreu
                    else:
                        print("Banco já cadastrado, tente novamente!")
            
            # Cadastra conta com cliente existente
            else:
                banco = bancos[opcao-1]
            
            # Retornando objeto da classe pessoa
            return Banco(banco)


def cadastro_cliente() -> tuple:
    """Cadastro de Novo Cliente

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (tuple):
            [0] (bool): Indicação se cadastro teve sucesso;
            [1] (str): Mensagem de confirmação.
    """
    # Capta nome/cpf do cliente
    print("\n" + f"{' Cadastro de Novo Cliente ':-^50}")
    nome = input("\nNome: ")
    cpf = input("CPF: ")
    
    # Cria objeto
    p = Pessoa(nome, cpf)
    
    # Realiza o cadastro
    res = DataSaver().cadastrar_cliente(p, PESSOAS_PATH)
    
    # Retorno o resultado
    return res


def cadastro_banco() -> tuple:
    """Cadastro de Banco

    > Argumentos:
        - Sem argumentos.

    > Output:
        - (tuple):
            [0] (bool): Indicação se cadastro teve sucesso;
            [1] (str): Mensagem de confirmação.
    """
    # Cria objeto Banco
    print("\n" + f"\n {' Cadastro de Novo Banco ':-^50}")
    b = Banco(input("\nNome do Banco: "))
    
    # Realiza o cadastro
    res = DataSaver().cadastrar_banco(b, BANCOS_PATH)
    
    # Retorno o resultado
    return res


def cadastro_conta(p:Pessoa, b:Banco, saldo:float=0) -> tuple:
    """Cadastro de Nova Conta Bancária

    > Argumentos:
        - p (Pessoa): Titular da conta;
        - b (Banco): Banco da conta;
        - saldo (float): Saldo inicial da conta, em R$.
            ----> Default: R$ 0,00
    
    > Output:
        - (tuple):
            [0] (bool): Indicação se cadastro teve sucesso;
            [1] (str): Mensagem de confirmação.
    """
    # pass
    print("\n" + f"{' Cadastro de Nova Conta ':-^50}")
    c = Conta(p, b, 0)

    # Realiza o cadastro
    res = DataSaver().cadastrar_conta(c, CONTAS_PATH)

    # Retorno o resultado
    return res


def cabecalho_resumo(texto:str):
    """Apresenta cabeçalho para os resumos

    > Argumento:
        - texto (str): Título do cabeçalho.
    
    > Output:
        - Sem output.
    """
    # Apresenta cabecalho
    print("\n" + "*"*50)
    print(f"{texto:^50}")
    print("*"*50 + "\n")


def rodape_resumo():
    """Apresenta cabeçalho para os resumos

    > Argumento:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresenta rodapé
    print("*"*50 + "\n")


def clientes_cadastrados(file_path:str):
    """Apresentar Clientes Cadastrados

    > Argumentos:
        - file_path (str): Caminho para arquivo contendo dados.

    > Output:
        - Sem output. 
    """
    # Resgatar lista de clientes
    clientes = listar_registros(file_path)

    # Apresenta cabecalho
    cabecalho_resumo()
    
    # Apresenta lista de clientes
    if len(clientes) == 0:
        print(f"  > Nenhum cliente cadastrado!")

    else:
        # Lista de clientes em ordem alfabética
        clientes = sorted([cliente.split(";")[::-1] for cliente in clientes])
        
        # Apresentar lista de clientes
        for cliente in clientes:
            print(f"  > {cliente[0]} [CPF: {cliente[1]}]")
    
    # Rodapé
    rodape_resumo()


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
        opcao = ler_opcao(1, len(opcoes_menu), "\nDigite um opção: ")

        # Cadastrar Pessoa
        if opcao == 1:
            res = cadastro_cliente()
            print(res[1])
            print("-"*50)
              
        # Cadastrar Banco
        elif opcao == 2:
            res = cadastro_banco()
            print(res[1])
            print("-"*50)
        
        # Cadastrar Nova Conta
        elif opcao == 3:
            p = selecionar_cliente(PESSOAS_PATH)    # Pessoa
            b = selecionar_banco(BANCOS_PATH)       # Banco
            s = 0                                   # Saldo
            # s = ler_float("\nSaldo inicial (R$): ", 0)
            res = cadastro_conta(p, b, s)
            print(res[1])
            print("-"*50)
        
        # Listar Clientes Cadastrados
        elif opcao == 4:
            clientes_cadastrados(PESSOAS_PATH)

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
    