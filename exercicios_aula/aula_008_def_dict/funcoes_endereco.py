# Cria lista para armazenar informacoes de endereco
# enderecos = []
enderecos = [
    {
        "id": 0, 
        "rua": "Antônio da Veiga", 
        "numero": "200", 
        "complemento": "Apto 104",
        "bairro": "Victor Konder",
        "cidade": "Blumenau",
        "estado": "SC"
    },
    {
        "id": 1, 
        "rua": "General Osorio", 
        "numero": "1890", 
        "complemento": "Apto 1007",
        "bairro": "Velha",
        "cidade": "Blumenau",
        "estado": "SC"
    },
    {
        "id": 2, 
        "rua": "Gustavo Zimmerman", 
        "numero": "980", 
        "complemento": "Apto 306",
        "bairro": "Itoupava Central",
        "cidade": "Blumenau",
        "estado": "SC"
    }
]


def cadastrar_endereco(
        id_pessoa:int, rua:str, numero:str, complemento:str, 
        bairro:str, cidade:str, estado:str) -> str:
    """Cadastro de Endereço.

    > Argumentos:
        - id_pessoa (int): ID do cliente;
        - rua (str): Nome da Rua;
        - numero (str): Número do imóvel onde o cliente reside;
        - complemento (str): Complemento ao número do imóvel (ex: Apt);
        - bairro (str): Bairro onde o cliente reside;
        - cidade (str): Cidade onde o cliente reside;
        - estado (str): Estado onde o cliente reside.
    
    > Output
        - Mensagem (str) indicando se o cadastro foi realizado ou não.
    """
    # Cria lista com parametros para testar condicao
    params = [id_pessoa, rua, numero, complemento, bairro, cidade, estado]

    # Testa se todos os dados estão preenchidos antes de realizar o cadastro
    if "" in params or None in params:
        return 0, "Cadastro de endereco falhou, faltam dados!"
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
        return 1, "Cadastrado realizado com sucesso!"


def enderecos_cadastrados() -> list:
    """Retorna todos os endereços cadastrados.
    
    > Argumentos:
        - Sem argumentos.
    
    > Output
        - Lista (list) de dicionários com endereços cadastrados.
    """
    return enderecos


def endereco_cliente(id_pessoa:int) -> dict:
    """Retorna endereço de acordo com ID.
    
    > Argumentos:
        - id_pessoa (int): ID do cliente que se deseja o endereço.
    
    > Output
        - Dicionário (dict) com o endereco do cliente indicado.
    """
    # Retorn endereco de acordo com ID
    for endereco in enderecos:
        if endereco['id'] == id_pessoa:
            return endereco
