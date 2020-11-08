"""
Entra21 Blusoft 2020 - Formação em Python

Autores: Marcus Moresco Boeno e Maria Vitória Machado
Data: 2020-10-09

Cadastro básico de clientes e endereços utilizando:
    - Listas
    - Dicionários
    - Funções
"""

# Importando funcoes
from funcoes_pessoa import cadastrar_pessoa, pessoas_cadastradas, cadastro_cliente 
from funcoes_endereco import cadastrar_endereco, enderecos_cadastrados, endereco_cliente

# Apresenta cabecalho do sistema
print("\n" + "*"*90)
print(f"{'Bem Vindo ao Cadastro de Clientes 1.0!':^90}")
print("*"*90)

while True:

    # Apresenta quantidade de clientes cadastrados
    print(f"\n> {len(pessoas_cadastradas())} clientes cadastrados")
    
    # Capta input do usuario quanto a terminar a execucao ou continuar
    while True:
        res = input("Deseja cadastrar novo cliente?! ([s]/n) ").strip().lower()
        if res in "sn":
            break
    
    # Cadastro de novo cliente
    if res in "s":
        print("\n>>> Cadastrando novo cliente:\n")

        # Coletando dados pessoas
        print("--- Dados pessoais:")
        nome = input("Nome: ").strip()
        sobrenome = input("Sobrenome: ").strip()
        idade = int(input("Idade: ").strip())

        # Realizando cadastro
        res_cad = cadastrar_pessoa(nome, sobrenome, idade)

        # Checa se cadastro foi realizado com sucesso
        if type(res_cad) is str:
            print("\n" + res_cad + "\n")
            print("-"*90 + "\n")
        else:
            while True:
                # Se cadastro realizado com sucesso, registrar endereco
                print("\n--- Endereço:")
                rua = input("Rua: ").strip()
                numero = input("Número: ").strip()
                complemento = input("Complemento: ").strip()
                bairro = input("Bairro: ").strip()
                cidade = input("Cidade: ").strip()
                estado = input("Estado: ").strip()

                # Realizando cadastro de endereco
                res_endereco = cadastrar_endereco(
                    res_cad, rua, numero, complemento, bairro, cidade, estado
                    )
                
                # Apresenta mensagem se cadastro foi concluído ou não
                if res_endereco[0] == 0:
                    print("\n" + res_endereco[1] + "\n")
                    print("Refazendo cadastro de endereço ...")
                else:
                    print("\n" + res_endereco[1] + "\n")
                    print("-"*90 + "\n")
                    break
    
    # Apresentacao dos clientes em tela e termino da execucao
    else:
        print("\n>>> Apresentando Cadastros:")

        # Apresenta cabecalho
        print("\n" + "*"*90)
        print(f"{'CLIENTES CADASTRADOS':^90}")
        print("*"*90 + "\n")
        
        # Recupera lista de clientes
        clientes = pessoas_cadastradas()

        # Itera sobre clientes
        for cliente in clientes:
            id_cliente = cliente['id']
            endereco = endereco_cliente(id_cliente)
            print(f"> Cliente #{id_cliente}")
            print(f"    Nome: {cliente['nome']} {cliente['sobrenome']}")
            print(f"    Idade: {cliente['idade']} anos")
            print(
                "    Endereço: {}, {}, {}, {}, {}-{}\n".format(
                    endereco['rua'],
                    endereco['numero'],
                    endereco['complemento'],
                    endereco['bairro'],
                    endereco['cidade'],
                    endereco['estado'],
                )
            )
        
        # Apresenta rodape
        print("*"*90 + "\n")

        # Apresenta mensagem de fim de execução
        print("Saindo do sistema, até logo...\n")
        break
