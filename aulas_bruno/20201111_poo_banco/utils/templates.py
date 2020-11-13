"""
Programação Orientada a Objetos (POO)
    - Templates para cabeçalhos e rodapés

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-13

"""


def cabecalho_resumo(texto:str):
    """Apresenta cabeçalho para os resumos

    > Argumento:
        - texto (str): Título do cabeçalho.
    
    > Output:
        - Sem output.
    """
    # Apresenta cabecalho
    print("\n" + "*"*50)
    print(f"{texto:^50}")
    print("*"*50 + "\n")


def rodape_resumo():
    """Apresenta cabeçalho para os resumos

    > Argumento:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresenta rodapé
    print("\n" + "*"*50 + "\n")


def cabecalho_menu(titulo:str):
    """Cabeçalho do Menu Principal

    > Argumentos:
        - titulo (str): Título do cabeçalho.
    
    > Output>
        - Sem output.
    """
    # Apresenta cabecalho
    print("\n" + "=-"*25)
    print(f"\n{titulo:^50}\n")
    print("=-"*25)