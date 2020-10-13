# Standard Library Import
import os

# Cria lista para armazenar cadastro de clientes
DADOS_ENDERECOS = "dados_enderecos.txt"


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
        # Salva informacoes de endereco no arquivo base
        with open(DADOS_ENDERECOS, "a") as f:
            f.write(
                "{};{};{};{};{};{};{}\n".format(
                    id_pessoa, rua, numero, complemento, bairro, cidade, estado
                    )
                )
        return 1, "Cadastrado realizado com sucesso!"


def enderecos_cadastrados() -> list:
    """Retorna todos os endereços cadastrados.
    
    > Argumentos:
        - Sem argumentos.
    
    > Output
        - Lista (list) de strings com endereços cadastrados.
    """
    # Tenta recuperar informações para gerar ID
    if os.path.isfile(DADOS_ENDERECOS):
        # Le informacoes armazenadas no arquivo base
        with open(DADOS_ENDERECOS, "r") as f:
            return [e.strip() for e in f.readlines()]
    else:
        # Se arquivo nao for encontrado retorna lista vazia
        return []


def endereco_cliente(id_pessoa:int) -> str:
    """Retorna endereço de acordo com ID.
    
    > Argumentos:
        - id_pessoa (int): ID do cliente que se deseja o endereço.
    
    > Output
        - String com os dados do cliente indicado.
    """
    # Tenta recuperar informações para gerar ID
    if os.path.isfile(DADOS_ENDERECOS):
        # Le informacoes armazenadas no arquivo base
        with open(DADOS_ENDERECOS, "r") as f:
            dados = [p.strip() for p in f.readlines()]
        return [p for p in dados if int(p.split(";")[0]) == id_pessoa][0]
    else:
        # Se arquivo nao for encontrado retorna string vazia
        return ""
