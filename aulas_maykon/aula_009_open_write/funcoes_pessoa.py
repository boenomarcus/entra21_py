# Standard Library Import
import os

# Cria lista para armazenar cadastro de clientes
DADOS_PESSOAS = "dados_pessoas.txt"


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

        # Tenta recuperar informações para gerar ID
        if os.path.isfile(DADOS_PESSOAS):
            # Se arquivo existe, id_pessoa = len(readlines()) 
            with open(DADOS_PESSOAS, "r") as f:
                id_pessoa = len(f.readlines())
        else:
            # Se arquivo nao for encontrado id_pessoa = 0
            id_pessoa = 0

        # Salva informacoes no arquivo base
        with open(DADOS_PESSOAS, "a") as f:
            f.write("{};{};{};{}\n".format(id_pessoa, nome, sobrenome, idade))
        
        # Retornando ID
        return id_pessoa


def pessoas_cadastradas() -> list:
    """Retorna dados de todos os clientes cadastrados.
    
    > Argumentos:
        - Sem argumentos.
    
    > Output
        - Lista (list) de strings com pessoas cadastradas.
    """
    # Tenta recuperar informações para gerar ID
    if os.path.isfile(DADOS_PESSOAS):
        # Le informacoes armazenadas no arquivo base
        with open(DADOS_PESSOAS, "r") as f:
            return [p.strip() for p in f.readlines()]
    else:
        # Se arquivo nao for encontrado retorna lista vazia
        return []  


def cadastro_cliente(id_pessoa:int) -> str:
    """Retorna cadastro de cliente de acordo com ID.
    
    > Argumentos:
        - id_pessoa (int): ID do cliente.
    
    > Output
        - String com os dados do cliente indicado.
    """
    # Tenta recuperar informações para gerar ID
    if os.path.isfile(DADOS_PESSOAS):
        # Le informacoes armazenadas no arquivo base
        with open(DADOS_PESSOAS, "r") as f:
            dados = [p.strip() for p in f.readlines()]
        return [p.strip() for p in dados if int(p.split(";")[0]) == id_pessoa][0]
    else:
        # Se arquivo nao for encontrado retorna string vazia
        return ""
