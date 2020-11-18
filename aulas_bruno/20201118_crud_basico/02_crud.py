import sys
from classes import Pessoa, Veiculo 


# Funções clientes
def cadastro_clinte():
    pass
def listar_clientes():
    pass
def alterar_cadastro_cliente():
    pass
def deletar_cliente():
    pass


# Funções veículos
def cadastro_veiculo():
    pass
def listar_veiculos():
    pass
def alterar_cadastro_veiculo():
    pass
def deletar_veiculo():
    pass


def menu_pessoas():
    while True:
        print(" >> Dados do cliente!")
        opcao = input("""
        [1] Cadastrar novo cliente
        [2] Listar clientes cadastrados
        [3] Alterar cadastro de cliente
        [4] Deletar cadastro de cliente

        [8] Voltar ao menu principal
        [9] Sair do sistema

        Digite uma opção: """)

        if opcao == "1":
            cadastro_clinte()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            alterar_cadastro_cliente()
        
        elif opcao == "4":
            deletar_cliente()
        
        elif opcao == "8":
            print("Retornando ao menu principal ...")
            break
        
        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        
        else:
            print("Opção inválida!")


def menu_veiculos():
    while True:
        print(" >> Dados dos veículos!")
        opcao = input("""
        [1] Cadastrar novo veículo
        [2] Listar veículos cadastrados
        [3] Alterar cadastro de veículo
        [4] Deletar cadastro de veículo

        [8] Voltar ao menu principal
        [9] Sair do sistema

        Digite uma opção: """)

        if opcao == "1":
            cadastro_veiculo()

        elif opcao == "2":
            listar_veiculos()

        elif opcao == "3":
            alterar_cadastro_veiculo()
        
        elif opcao == "4":
            deletar_veiculo()
        
        elif opcao == "8":
            print("Retornando ao menu principal ...")
            break
        
        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        
        else:
            print("Opção inválida!")

def main():
    while True:
        print(" >> Bem vindo ao sistema CRUD 1.0!")
        opcao = input("""
        [1] Pessoas
        [2] Veículos

        [9] Sair do sistema

        Digite uma opção: """)

        if opcao == "1":
            menu_pessoas()

        elif opcao == "2":
            menu_veiculos()

        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()



