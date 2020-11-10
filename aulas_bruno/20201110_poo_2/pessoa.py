"""
Programação Orientada a Objetos (POO)
- Herança e Polimorfismo
- Classe Pessoa

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-10

"""


class Pessoa:
    """Pessoa

    > Argumentos:
        - nome (str): Nome 
        - idade (int): Idade
        - cpf (str): CPF sem pontos nem traços
    """
    # Método construtor
    def __init__(self, nome:str, idade:int, cpf:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    