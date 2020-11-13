"""
Programação Orientada a Objetos (POO)
    - Validações e leituras de números int/float

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno e Helion Roloff
Último update: 2020-11-13

"""

# Standard library imports
import sys


def ler_opcao(minimum:int, maximum:int, txt:str) -> int:
    """Ler opcao do Menu

    > Argumentos:
        - minimum (int): Valor mínimo para opção;
        - maximum (int): Valor máximo para opção;
        - txt (str): Texto a ser apresentado no momento da leitura;
    
    > Output:
        - (int): Opcao do menu indicada pelo usuario.
    """    
    # Realiza leitura da opcao do usuario e retorna quando valida
    while True:

        # Realiza leitura da opcao do usuario
        try:
            opcao = int(input(txt).strip())
        
        # Sai do jogo quando indicado pelo usuario
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo!...\n")
        
        # Exceção para valor inválido
        except ValueError:
            print("[ERRO] Entrada inválida, digite uma opção!")
        
        # Checa se entrada é valida
        else:
            # Se dominio é válido, retorna opção
            if minimum <= opcao <= maximum:
                return opcao
            
            # Indica opção inválida para erro no dominio
            print("[ERRO] Entrada inválida, digite uma opção!")


def ler_float(txt:str, minimum:float) -> float:
    """Ler número real (float)

    > Argumentos:
        - txt (str): Texto a ser apresentado no momento da leitura;
        - minimum (float): Valor mínimo aceitável.

    > Output:
        - (float): Valor indicado pelo usuario. 
    """
    # Realiza leitura da opcao do usuario e retorna quando valida
    while True:
        # Realiza leitura da opcao do usuario
        try:
            n = float(input(txt).strip())
        
        # Sai do sistema quando indicado pelo usuario
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo!...\n")
        
        # Exceção para valor inválido
        except ValueError:
            print("[ERRO] Entrada inválida!")
        
        # Checa se entrada é valida
        else:
            # Se dominio é válido, retorna valor
            if n >= minimum:
                return n
            
            # Indica valor inválido para erro no dominio
            print(f"[ERRO] Entrada inválida!")
