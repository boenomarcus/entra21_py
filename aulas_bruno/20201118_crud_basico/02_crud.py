

# Standard library import
import sys

# Importando classes e metodos
from classes import Cliente, Veiculo, DataReader, DataWriter 

# Indica caminho para arquivo com base de dados
DB_PATH = "clientes.db"


def menu_clientes():
    """Menu para trabalhar com dados dos clientes
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
            
            # Apresenta cabeçalho
            print("\n" + "*"*60)
            print(f"{'CLIENTES CADASTRADOS':^60}")
            print("*"*60 + "\n")

            if len(clientes) == 0:
                print(" > Nenhum cliente cadastrado!")
            else:
                for cliente in clientes:
                    print(f" > [ID: {cliente[0]}] {cliente[1]} (CPF: {cliente[3]})")

            # Apresenta rodapé
            print("\n" + "*"*60)    
                
        # Altera cadastro de cliente
        elif opcao == "3":
            alterar_cadastro_cliente()
            pass
        
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
    """Menu Veiculos
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
    """
    while True:
        print("\n >> Bem vindo ao sistema CRUD 1.0!")
        opcao = input("""
        Deseja manipular quais registros?

        [1] Pessoas
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
