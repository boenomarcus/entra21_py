"""
Entra21 Blusoft 2020 - Formação em Python

Autores: Marcus Moresco Boeno e Maria Vitória Machado
Data: 2020-10-09

Cadastro básico de clientes e endereços utilizando:
    - Listas
    - Dicionários
    - Funções
"""

# Importando Standard Libraries
import sys

# Importando funcoes
from funcoes_pessoa import cadastrar_pessoa, pessoas_cadastradas, cadastro_cliente 
from funcoes_endereco import cadastrar_endereco, enderecos_cadastrados, endereco_cliente

# Apresenta cabecalho do sistema
print("\n" + "*"*90)
print(f"{'Bem Vindo ao Cadastro de Clientes 1.0!':^90}")
print("*"*90)


def readInt(txt:str) -> int:
    """Leitura de numeros inteiros.

    > Argumentos:
        - txt: String para construção da chamada input().
    
    > Output:
        - int: Numero inteiro definido pelo usuario.
    """
    # Capta input do usuario e retorna quando válido
    while True:
        try:
            n = int(input(txt).strip())
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo! ...\n")
        except:
            print("[ERRO] Digite um numero inteiro!")
        else:
            return n


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
        idade = readInt("Idade: ")

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
                    print("-"*90)
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

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado!\n")
        else:
            # Itera sobre clientes
            for cliente in clientes:
                dados = cliente.split(";")
                endereco = endereco_cliente(dados[0]).split(";")
                print(f"> Cliente #{dados[0]}")
                print(f"    Nome: {dados[1]} {dados[2]}")
                print(f"    Idade: {dados[3]} anos")
                print(
                    "    Endereço: {}, {}, {}, {}, {}-{}\n".format(
                        endereco[1],
                        endereco[2],
                        endereco[3],
                        endereco[4],
                        endereco[5],
                        endereco[6],
                    )
                )
        
        # Apresenta rodape
        print("*"*90 + "\n")

        # Apresenta mensagem de fim de execução
        print("Saindo do sistema, até logo...\n")
        break
