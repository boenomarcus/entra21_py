"""
Sistema CRUD Básico: Clientes e Veículos
    - Interface Básica no Terminal

Blusoft/Senac - Formação em Python Entra21 2020

Autores:
    - Leonardo da Silva Kostetzer
    - Marcus Moresco Boeno
    - Thiago Augusto Zeferino

Último Update: 2020-11-21

"""

# Standard library import
import sys
from time import sleep

# Importando classes e metodos
from classes import Cliente, Veiculo, DataReader, DataWriter 

# Indica caminho para arquivo com base de dados
DB_PATH = "clientes.db"


def menu_clientes():
    """Menu para gestão da base de clientes

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresenta opções para menu de clientes
    while True:
        print("\n >> Dados do cliente!")
        opcao = input("""
        [1] Cadastrar novo cliente
        [2] Listar clientes cadastrados
        [3] Alterar cadastro de cliente
        [4] Deletar cadastro de cliente

        [8] Voltar ao menu principal
        [9] Sair do sistema

        Digite uma opção: """)

        # Realizar novo cadastro
        if opcao == "1":
            c = Cliente(
                input("Digite nome cliente: "),
                input("Digite o cpf: "), 
                input("Digite o email: ")
            )

            # Inserção do cliente no banco
            DataWriter(DB_PATH, "clientes").insert(c)

        # Apresentar clientes em tela
        elif opcao == "2":

            # Recupera informações de cliente    
            clientes = DataReader(DB_PATH, "clientes").retrieve_all()
            
            # Apresenta clientes cadastrados
            print("\n" + "="*60 + "\n")
            print(f"{'- LISTAGEM -':^60}" + "\n")
            print("="*60 + "\n")
            sleep(1)
            
            # Testa se existem clientes na base
            if len(clientes) == 0:
                    print(' > Nenhum cliente cadastrado!')
            
            else:
                # Apresenta resumo das informações dos clientes cadastrados
                count = 0
                print(f"Existem {len(clientes)} Cliente(s) Cadastrado(s): ")
                for cliente in clientes:
                    count += 1
                    print("\n" + f"  - {count}°  C L I E N T E -")
                    print(f"    I D      |  {cliente[0]}")
                    print(f"    N O M E  |  {cliente[1]}")
                    print(f"    C P F    |  {cliente[3]}")
            
            # Rodapé
            print("\n" + "="*60)
                
        # Altera cadastro de cliente
        elif opcao == "3":
            DataWriter(DB_PATH, "clientes").update_info()
        
        # Deleta registro de cliente
        elif opcao == "4":
            deletar_cliente()
            pass
        
        # Retorna ao menu principal
        elif opcao == "8":
            print("\n        Retornando ao menu principal ...")
            break
        
        # Sai do sistema
        elif opcao == "9":
            sys.exit("\n        Saindo, até logo! ...\n")
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


def menu_veiculos():
    """Menu para gestão da base de veículos

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    while True:
        print("\n >> Dados dos veículos!")
        opcao = input("""
        [1] Cadastrar novo veículo
        [2] Listar veículos cadastrados
        [3] Alterar cadastro de veículo
        [4] Deletar cadastro de veículo

        [8] Voltar ao menu principal
        [9] Sair do sistema

        Digite uma opção: """)

        # Realizar novo cadastro
        if opcao == "1":
            pass
        
        # Apresentar veiculos em tela
        elif opcao == "2":
            pass
        
        # Altera cadastro de veiculo
        elif opcao == "3":
            pass
        
        # Deleta veiculo cadastro
        elif opcao == "4":
            pass
        
        # Retorna ao menu principal
        elif opcao == "8":
            print("\n        Retornando ao menu principal ...")
            break
        
        # Sai do sistema
        elif opcao == "9":
            sys.exit("\n        Saindo, até logo! ...\n")
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


def main_menu():
    """Menu Principal

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    while True:
        print("\n >> Bem vindo ao sistema CRUD 1.0!")
        opcao = input("""
        Deseja manipular quais registros?

        [1] Clientes
        [2] Veículos

        [9] Sair do sistema

        Digite uma opção: """)

        # Opção para trabalhar com tabela de clientes
        if opcao == "1":
            menu_clientes()

        # Opção para trabalhar com tabela de veiculos
        elif opcao == "2":
            menu_veiculos()

        # Opção para sair do sistema
        elif opcao == "9":
            print("\n        Saindo, até logo! ... \n")
            break
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


if __name__ == "__main__":
    # Inicializa sistema
    main_menu()
