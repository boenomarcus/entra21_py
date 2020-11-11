"""
Programação Orientada a Objetos (POO)

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-11

"""
# Standard Library imports
import sys

# Importando classes externas
from pessoa import Pessoa

# Constantes
BANCOS = [
    "NuBank", "Banco do Brasil", "Bradesco", "ViaCredi",
    "Itaú", "Santander", "Banrisul",
    ]


# class Pessoa:
#     """Pessoa

#     > Argumentos:
#         - nome (str): Nome 
#         - idade (int): Idade
#         - cpf (str): CPF sem pontos nem traços
#     """
#     # Método construtor
#     def __init__(self, nome:str, idade:int, cpf:str):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf
    
#     # Getter-Method para retornar nome da pessoa
#     def get_name(self):
#         """Getter-Method para retornar nome da pessoa

#         > Argumentos:
#             - Sem argumentos.
        
#         > Output:
#             - (str): Nome da pessoa.
#         """
#         # Retorna nome da pessoa
#         return self.nome.title()

# class Conta():
#     """Conta Bancária

#     Classe para a representação de uma conta bancária.

#     > Argumentos:
#         - banco (Banco): Instituição bancária da conta;
#         - pessoa (Pessoa): Titular da conta.
#     """
#     # Método construtor
#     def __init__(self, banco:Banco, pessoa:Pessoa):
#         self.banco = banco
#         self.pessoa = pessoa


# class Banco():
#     """Instituição Bancária

#     > Argumentos:
#         - nome (str): Nome Fantasia da instituição bancária.
#     """
#     # Método construtor
#     def __init__(self, nome:str):
#         self.nome = nome


def checa_se_ja_cadastrado(cpf):
    """Checa se CPF já está cadastrado

    > Argumentos:
        - cpf (str): Cadastro de Pessoa Física (CPF).
    
    > Output:
        - (bool): Indicação se CPF já está cadastrado.
    """
    # Recupera CPFs cadastrados
    with open("data/pessoas.txt", "r") as f:
        cpfs = [x.split(";")[0] for x in f.read().splitlines()]
    
    # Verifica se CPF já cadastrado
    if cpf in cpfs:
        return True
    else:
        return False


def cadastro_pessoa():
    """Cadastrar de Pessoa

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem argumentos.
    """
    # Capta CPF
    cpf = input("CPF: ")

    # Verifica se CPF já está cadastrado
    if not checa_se_ja_cadastrado(cpf):

        # Se não cadastrado, capta nome e finaliza o cadastro
        nome = input("Nome: ")
        with open("data/pessoas.txt", "a+") as f:
            f.write(
                f"{cpf};{nome}\n"
            )
    
    # Indica que o CPF já está cadastrado
    else:
        print(f"CPF {cpf} já cadastrado!")


def ler_opcao(opcoes_menu:list, txt:str):
    """Ler opcao do Menu

    > Argumentos:
        - opcoes_menu (list): Opções do menu.
        - txt (str): Texto a ser apresentado no momento da leitura;
    
    > Output:
        - (int): Opcao do menu indicada pelo usuario.
    """    
    # Detecta numero de opcoes validas
    num_opcoes = len(opcoes_menu)
    
    # Realiza leitura da opcao do usuario e retorna quando valida
    while True:

        # Realiza leitura da opcao do usuario
        try:
            opcao = int(input(txt).strip())
        
        # Sai do jogo quando indicado pelo usuario
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo!...\n")
        
        # Exceção para valor inválido
        except ValueError:
            print("[ERRO] Entrada inválida, digite uma opção!")
        
        # Checa se entrada é valida
        else:
            # Se dominio é válido, retorna opção
            if 0 < opcao < num_opcoes + 1:
                return opcao
            
            # Indica opção inválida para erro no dominio
            print("[ERRO] Entrada inválida, digite uma opção!")


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
            "Cadastrar Pessoa",
            "Cadastrar Conta",
            "Visualizar Saldo",
            "Realizar Saque",
            "Realizar Depósito",
            "Sair do sistema",
            ]

        # Apresentar menu e captar opcao do usuario
        apresentar_menu(opcoes_menu)
        opcao = ler_opcao(opcoes_menu, "\nDigite um opção: ")

        # Cadastrar pessoa
        if opcao == 1:
            cadastro_pessoa()
        
        # Cadastrar Conta
        elif opcao == 2:
            cadastro_conta()
        
        # Visualizar saldo
        elif opcao == 3:
            saldo()
        
        # Realizar saque
        elif opcao == 4:
            saque()
        
        # Realizar deposito
        elif opcao == 5:
            deposito()
        
        # Sair do sistema
        elif opcao == 6:
            sys.exit("\nSaindo, até logo!...\n")

        # Indicar opção inválida
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":

    # Executar sistema se estiver no namespace principal
    main()
    