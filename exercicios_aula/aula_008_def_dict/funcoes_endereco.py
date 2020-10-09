
enderecos = []

def cadastrar_endereco(id_pessoa, rua, numero, complemento, bairro, cidade, estado):
    #--- Exercício 2  - Funções
    #--- Escreva uma função para cadastro de endereço:
    #---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
    #---       a função deve salvar os dados de endereço em uma lista com escopo global
    #---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos (str vazia ou None)
    #---       a função deve retornar uma mensagem ao final de acordo com a situação
    #--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
    if id_pessoa == "" or rua == "" or numero == "" or complemento == "" or bairro == "" or cidade == "" or estado == "":
        return "Cadastro de endereco falhou, faltam dados!"
    else:
        endereco = {}
        endereco["id"] = id_pessoa
        endereco["rua"] = rua
        endereco["numero"] = numero
        endereco["complemento"] = complemento
        endereco["bairro"] = bairro
        endereco["cidade"] = cidade
        endereco["estado"] = estado
        enderecos.append(endereco)
        return "Endereço cadastrado com sucesso!"

def exibir_enderecos():
    #--- Escreva uma função para listar endereços cadastrados:
    #---    a função deve exibir todos os endereços cadastrados na função do ex2
    print("\n" + "*"*50)
    print(f"{'PESSOAS CADASTRADAS':^50}")
    print("*"*50 + "\n")
    for endereco in enderecos:
        print(f"[ID: {endereco['id']}] ")
    print("\n" + "*"*50 + "\n")

def exibir_endereco():
    #--- Escreva uma função para exibir um endereço específico:
    #        a função deve exibir um endereço cadastrado na função do ex2 filtrando por 
    #        id da pessoa
    pass