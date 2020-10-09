
pessoas = []

def cadastrar_pessoa(nome, sobrenome, idade):
    #--- Exercício 1  - Funções
    #--- Escreva uma função para cadastro de pessoa:
    #---       a função deve receber três parâmetros, nome, sobrenome e idade
    #---       a função deve salvar os dados da pessoa em uma lista com escopo global
    #---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
    #---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
    #---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
    #--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
    if idade < 18:
        return "Não é possível cadastrar! (Idade menor do que 18)"
    else:
        pessoa = {}
        pessoa["nome"] = nome
        pessoa["sobrenome"] = sobrenome
        pessoa["idade"] = idade
        pessoa["id"] = len(pessoas)
        pessoas.append(pessoa)
        return f"Cadastro realizado com sucesso (id = {pessoa['id']})"

def exibir_pessoas():
    #--- Escreva uma função para listar pessoas cadastradas:
    #---    a função deve exibir todas as pessoas cadastradas na função do ex1
    print("\n" + "*"*50)
    print(f"{'PESSOAS CADASTRADAS':^50}")
    print("*"*50 + "\n")
    for pessoa in pessoas:
        print(f"[ID: {pessoa['id']}] {pessoa['nome']} {pessoa['sobrenome']} ({pessoa['idade']} anos)")
    print("\n" + "*"*50 + "\n")


def exibir_pessoa(id_pessoa):
    #--- Escreva uma função para exibi uma pessoa específica:
    #    a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id
    print("\n" + "*"*50)
    print(f"{'CADASTRO PESSOA':^50}")
    print("*"*50 + "\n")
    for pessoa in pessoas:
        if pessoa['id'] == id_pessoa:
            print(f"[ID: {pessoa['id']}] {pessoa['nome']} {pessoa['sobrenome']} ({pessoa['idade']} anos)")
    print("\n" + "*"*50 + "\n")