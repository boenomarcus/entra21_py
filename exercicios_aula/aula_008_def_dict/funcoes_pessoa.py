
# Cria lista para armazenar cadastro de clientes
# pessoas = []
pessoas = [
    {"nome": "Marcus", "sobrenome": "Boeno", "idade": 26, "id": 0},
    {"nome": "Maria", "sobrenome": "Vitoria", "idade": 18, "id": 1},
    {"nome": "Pedro", "sobrenome": "Carvalho", "idade": 34, "id": 2}
]


def cadastrar_pessoa(nome:str, sobrenome:str, idade:int):
    """Cadastro de Cliente.

    > Argumentos:
        - nome (int): Primeiro nome do cliente;
        - sobrenome (str): Sobrenome do cliente;
        - idade (int): Idade, em anos, do cliente.

    > Output
        - Mensagem (str) ou ID do cadastro.
    """
    if idade < 18:
        return "Não é possível cadastrar! (Idade menor do que 18)"
    else:
        pessoa = {}
        id_pessoa = len(pessoas)
        pessoa["nome"] = nome
        pessoa["sobrenome"] = sobrenome
        pessoa["idade"] = idade
        pessoa["id"] = id_pessoa
        pessoas.append(pessoa)
        return id_pessoa


def pessoas_cadastradas() -> list:
    """Retorna dados de todos os clientes cadastrados.
    
    > Argumentos:
        - Sem argumentos.
    
    > Output
        - Lista (list) de dicionários com pessoas cadastradas.
    """
    return pessoas


def cadastro_cliente(id_pessoa:int) -> dict:
    """Retorna cadastro de cliente de acordo com ID.
    
    > Argumentos:
        - id_pessoa (int): ID do cliente.
    
    > Output
        - Dicionário (dict) com o cadastro do cliente indicado.
    """
    return pessoas[id_pessoa]