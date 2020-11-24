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
            print("\n --- CADASTRO DE CLIENTE --- \n")
            c = Cliente(
                input("Nome: "),
                input("Data de Nascimento (aaaammdd): "), 
                input("CPF: "),
                input("Endereço: "),
                float(input("Salário: R$ ")),
                input("Profissão: "),
                input("Email: "),
                input("Telefone: "),
                input("Responsável: "),
                input("Sexo: "),
                input("Naturalidade: "),
                input("Nacionalidade: ")
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
                       
            # Testa se existem clientes na base
            if len(clientes) == 0:
                    print(' > Nenhum cliente cadastrado!')
            
            else:
                # Apresenta resumo das informações dos clientes cadastrados
                count = 0
                print(f"Existem {len(clientes)} Cliente(s) Cadastrado(s): ")

                # Aplica filtros para apresentação dos clientes
                print('\n\nEscolha Uma Opção De Visualização:')
                
                # Cria conexão com DB
                conectar = sqlite3.connect(DB_PATH)

                # Cria cursor para interação com o DB
                cursor = conectar.cursor()

                while True:

                    opcao_visualizar = input(''' 
    1 - Filtrar Por Nome
    2 - Filtrar Por Naturalidade
    3 - Filtrar Por CPF
    4 - Ver Todos
    5 - Sair Da Visualização

    Digite o Número Respectivo a Ação Que Deseja:\n   R:  ''')

                    # Realiza filtragem por nome                        
                    if opcao_visualizar == '1':
                        count = 0
                        qual_nome = input('\nDigite Um Nome ou letra(s): ').capitalize()
                        cursor.execute(f'''
SELECT * FROM clientes
WHERE nome LIKE '{qual_nome}%';
''')                    
                        dados = cursor.fetchall()

                        if len(dados) == 0:
                            print(f'\nNão Foi Encontrado Nenhum {qual_nome}!')
                        else:
                            print('\n=========================================================')
                            for linha in dados:
                                count += 1
                                print(f'''
        - {count}°  C L I E N T E -
    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')

                            print('\n=========================================================')

                        qualquer = input('Aperte Enter Para Continuar: ')

                    # Realiza filtragem por cidade
                    elif opcao_visualizar == '2':
                        count = 0
                        qual_cidade = input('\nDigite Uma Cidade: ')
                        cursor.execute(f'''
SELECT * FROM clientes
WHERE naturalidade LIKE '%{qual_cidade}%';
''')                    
                        dados = cursor.fetchall()

                        if len(dados) == 0:
                            print(f'\nNão Foi Encontrado Nenhuma Cidade com nome de {qual_cidade}!')
                        else:
                            print('\n=========================================================')
                            for linha in dados:
                                count += 1
                                print(f'''
        - {count}°  C L I E N T E -
    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                            print('\n=========================================================')
                            qualquer = input('Aperte Enter Para Continuar: ')
                        
                    # Realiza filtragem por CPF
                    elif opcao_visualizar == '3':
                        count = 0
                        qual_cpf = input('\nDigite Um CPF: ')
                        cursor.execute(f'''
SELECT * FROM clientes
WHERE cpf LIKE '%{qual_cpf}%';
''')                    
                        dados = cursor.fetchall()

                        if len(dados) == 0:
                            print(f'\nNão Foi Encontrado Nenhum CPF Com Esses Números: {qual_cpf}!')
                        else:
                            print('\n=========================================================')
                            for linha in dados:
                                count += 1
                                print(f'''
        - {count}°  C L I E N T E -
    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                            print('\n=========================================================')
                            qualquer = input('Aperte Enter Para Continuar: ')


                    # Apresenta todos os clientes
                    elif opcao_visualizar == '4':
                        count = 0
                        # Apresenta Os Dados Da Função
                        for linha in clientes:
                            count += 1
                            print(f'''
        - {count}°  C L I E N T E -
    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                        qualquer = input('Aperte Enter Para Continuar: ')

                    # Sair do sistema de filtragem
                    elif opcao_visualizar == '5':
                        print('\nSaindo...')
                        break
                        
                    else:
                        print('\n', '=' * 15, 'Incorreto!', '=' * 15)

                # Apresentação básico de cadastro
                # for cliente in clientes:
                #     count += 1
                #     print("\n" + f"  - {count}°  C L I E N T E -")
                #     print(f"    I D      |  {cliente[0]}")
                #     print(f"    N O M E  |  {cliente[1]}")
                #     print(f"    C P F    |  {cliente[3]}")
            
            # Rodapé
            print("\n" + "="*60)
                
        # Altera cadastro de cliente
        elif opcao == "3":
            DataWriter(DB_PATH, "clientes").update_info()
        
        # Deleta registro de cliente
        elif opcao == "4":
            DataWriter(DB_PATH, "clientes").delete_registry()
                    
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
            print("\n --- CADASTRO DE VEÍCULO --- \n")
            v = Veiculo(
                input("Nome: "),
                input("Marca: "), 
                input("Modelo: "),
                input("Ano: "),
                input("Placa: "),
                int(input("Número de Portas: ")),
                input("Cor: "),
                input("Quilometragem (km): "),
                int(input("Máximo de Passageiros: ")),
                int(input("Potência do Motor (CV): ")),
                input("Combustível: "),
                input("Força Motriz: "),
                float(input("Valor (R$): ")),
                int(input("ID do cliente: "))
            )

            # Inserção de um veículo no banco
            DataWriter(DB_PATH, "veiculos").insert(v)
        
        # Apresentar veiculos em tela
        elif opcao == "2":
            # Recupera informações de cliente    
            veiculos = DataReader(DB_PATH, "veiculos").retrieve_all()
            
            # Apresenta veiculos cadastrados
            print("\n" + "="*60 + "\n")
            print(f"{'- VEÍCULOS CADASTRADOS -':^60}" + "\n")
            print("="*60 + "\n")

            # Testa se existem veiculos na base
            if len(veiculos) == 0:
                    print(' > Nenhum veículo cadastrado!')
            
            else:
                # Apresenta resumo das informações dos veículos cadastrados
                print(f"Existem {len(veiculos)} Veículo(s) Cadastrado(s):\n")
                for veiculo in veiculos:
                    print(
                        "  > [ID: {}] {} {} (Placa: {})".format(
                            veiculo[0], veiculo[2], veiculo[1], veiculo[5]
                        )
                        )
            
            # Rodapé
            print("\n" + "="*60)
        
        # Altera cadastro de veiculo
        elif opcao == "3":
            DataWriter(DB_PATH, "veiculos").update_info()
        
        # Deleta veiculo cadastro
        elif opcao == "4":
            DataWriter(DB_PATH, "veiculos").delete_registry()
        
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
