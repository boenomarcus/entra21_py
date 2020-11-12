"""
Programação Orientada a Objetos (POO)
    - Validações e leituras de números int/float

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-12

"""

# Standard library imports
import sys


def ler_opcao(opcoes_menu:list, txt:str) -> int:
    """Ler opcao do Menu

    > Argumentos:
        - opcoes_menu (list): Opções do menu.
        - txt (str): Texto a ser apresentado no momento da leitura;
    
    > Output:
        - (int): Opcao do menu indicada pelo usuario.
    """    
    # Detecta numero de opcoes validas
    num_opcoes = len(opcoes_menu)
    
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
            if 0 < opcao < num_opcoes + 1:
                return opcao
            
            # Indica opção inválida para erro no dominio
            print("[ERRO] Entrada inválida, digite uma opção!")


def ler_float(txt:str, min:float) -> float:
    """Ler número real (float)

    > Argumentos:
        - txt (str): Texto a ser apresentado no momento da leitura;
        - min (float): Valor mínimo aceitável.

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
            if n >= min :
                return n
            
            # Indica valor inválido para erro no dominio
            print(f"[ERRO] Entrada inválida!")
