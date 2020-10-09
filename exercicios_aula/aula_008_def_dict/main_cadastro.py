#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4

# Importando variaveis
from funcoes_pessoa import pessoas
from funcoes_endereco import enderecos

# Importando funcoes
from funcoes_pessoa import cadastrar_pessoa, exibir_pessoas, exibir_pessoa
from funcoes_endereco import cadastrar_endereco, exibir_enderecos, exibir_endereco

print("\n" + "=-"*30 + "\n")

while True:

    # Opções para o menu principal
    menu = [
        "Cadastrar Pessoa",
        "Cadastrar Endereço",
        "Exibir Pessoas Cadastradas",
        "Exibir Pessoa",
        "Exibir Endereços Cadastrados",
        "Exibir Endereço",
        "Sair",
    ]
    
    # Apresenta menu e capta opção do usuário
    print("-"*50)
    print(f"{'CADASTRO DE PESSOAS E ENDEREÇOS':^50}")
    print("-"*50)
    print("\n> Menu Principal:\n")
    for pos, opcao in enumerate(menu):
        print(f"[{pos+1}] {opcao}")
    # Define ação 
    opcao = input("\nDigite um opção: ").strip()

    # Cadastra Pessoa
    if opcao == "1":
        print("\n" + "-"*50 + "\n")
        print("> Cadastrar Pessoa:\n")
        nome = input("Nome: ").strip()
        sobrenome = input("Sobrenome: ").strip()
        idade = int(input("Idade: ").strip())
        print(cadastrar_pessoa(nome, sobrenome, idade))
        print("\n" + "-"*50 + "\n")
    
    # Cadastra Endereço
    elif opcao == "2":
        print("\n" + "-"*50 + "\n")
        print("> Cadastrar Endereço:\n")
        if len(pessoas) == 0:
            print("Nenhuma Pessoa Cadastrada!\n")
        else:
            print(f"IDs disponíveis = 0 a {len(pessoas)-1}\n")
            id_pessoa = int(input("ID: ").strip())

            if id_pessoa < 0 or id_pessoa > len(pessoas)-1:
                print("\nID (Pessoa) não cadastrada!")
                print("\n" + "-"*50 + "\n")
            else:
                rua = input("Rua: ").strip()
                numero = input("Número: ").strip()
                complemento = input("Complemento: ").strip()
                bairro = input("Bairro: ").strip()
                cidade = input("Cidade: ").strip()
                estado = input("Estado: ").strip()
                print(
                    cadastrar_endereco(
                        id_pessoa, 
                        rua, 
                        numero, 
                        complemento, 
                        bairro, 
                        cidade, 
                        estado
                        )
                    )

    # Exibir Pessoas Cadastradas
    elif opcao == "3":
        pass
    
    # Exibir Pessoa a partir de ID
    elif opcao == "4":
        pass
    
    # Exibir Endereços Cadastrados
    elif opcao == "5":
        pass
    
    # Exibir Endereco a partir de ID
    elif opcao == "6":
        pass
    
    # Saindo do sistema
    elif opcao == "7":
        print("\n" + "Saindo, até logo ...")
        break

print("\n" + "=-"*30 + "\n")