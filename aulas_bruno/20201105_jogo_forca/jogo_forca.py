"""
Jogo da Forca 1.0!

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Marcus Moresco Boeno
Último update: 2020-11-08

"""

# Standard library imports
import os
import sys
import pathlib
import random

# Define constantes
FILE_PATH = pathlib.Path(__file__).parent.absolute()
CARACTERES = "abcdefghijklmnopqrstuvxywzç"

# Define dificuldade inicial do jogo
nivel = "Aleatório"


def carrega_config(dif:str) -> tuple:
    """Carrega configurações

    > Argumentos:
        - dif (str): Nível de dificuldade.
            ---> Opções: ["Fácil", "Difícil", "Aleatório"].
    
    > Output:
        - (tuple): Tupla com palavra e numero de chances
    """
    # Fácil
    if dif == "Fácil": 
        dados, chance = "palavras_facil.txt", 7

    # Aleatório
    elif dif == "Aleatório":
        dados, chance = "palavras_aleatorio.txt", 6
    
    # Difícil
    elif dif == "Difícil":
        dados, chance = "palavras_dificil.txt", 5    
    
    # Retornando palavra e numero de chances
    with open(os.path.join(FILE_PATH, dados), "r", encoding="utf-8") as f:
        return random.choice(f.read().splitlines()).lower(), chance


def ler_letra(letras_usadas:list) -> str:
    """Leitura e validação de letras

    > Argumentos:
        - letras_usadas (list): Lista indicando as letras já utilizadas.
    
    > Output:
        - (str): Letra indicada pelo usuário
    """
    while True:
        try:
            letra = input("Digite uma letra: ").strip().lower()
        
        # Sai do jogo quando indicado pelo usuario
        except KeyboardInterrupt:
            print("\n\nSaindo do jogo, até logo!...\n")
            sys.exit()
        
        else:
            # Checando se input é igual a um caracter
            if len(letra) != 1:
                print("[ERRO] Entrada inválida, digite apenas uma letra!")
            
            # Checa se caracter é um caracter válido
            elif letra not in CARACTERES:
                print("[ERRO] Entrada inválida, digite uma letra!")
            
            # Checa se letra já foi utilizada
            elif letra in letras_usadas:
                print("[ERRO] Letra já utilizada, tente novamente!") 

            # Retorna letra se entrada for valida e ainda nao utilizada
            else:
                return letra


def limpar_tela():
    """Limpeza da tela

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada rodada
    # "cls" para windows e "clear" para linux/mac (posix)
    os.system('cls') if os.name == 'nt' else os.system('clear')


def atualiza_palavra(letras_usadas:list, palavra:str) -> str:
    """Atualiza partes já descobertas da palavra

    > Argumentos:
        - letras_usadas (list): Lista indicando as letras já utilizadas;
        - palavra (str): Palavra a ser descoberta pelo usuário.
    
    > Output:
        - (str): String com partes já descobertas da palavra.
    """
    # Declara string vazia para armazenar resultados
    tentativa_palavra = ""

    # Itera sobre palavra identificando partes já descobertas
    for x in palavra:
        tentativa_palavra += x if x in letras_usadas else "_"
    
    # Retornando string com partes já descobertas pelo usuario
    return tentativa_palavra


def verifica_fim_jogo(tentativa_palavra:str, palavra:str, chances:int) -> bool:
    """Verifica se rodada foi finalizada

    > Argumentos:
        - tentativa_palavra (str): Partes já descobertas da palavra;
        - palavra (str): Palavra a ser descoberta pelo usuário;
        - chances (int): Chances restantes.
    
    > Output:
        - (bool): Indicação se o jogo terminou (True) ou não (False).
    """
    # Palavra finalizada, usuario venceu!
    if tentativa_palavra == palavra:
        print(f"\nVocê ganhou restando {chances} tentativa(s)!")
        print(f"   > Palavra: {palavra}\n")
        print("-"*50)
        return True

    # Verifica se chances terminaram    
    elif chances == 0:
        print("\nVocê perdeu!")
        print(f"   > Palavra: {palavra}\n")
        print("-"*50)
        return True
    
    # Retorna False de jogo ainda não terminou
    return False

def apresenta_resumo(palavra:str, letras_usadas:list, chances:int):
    """Apresenta resumo da rodada

    > Argumentos:
        - palavra (str): Palavra a ser descoberta pelo usuário;
        - letras_usadas (list): Lista indicando as letras já utilizadas;
        - chances (int): Chances restantes.
    
    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada rodada
    limpar_tela()

    # Apresenta chance restantes e letras já utilizadas
    print("\n" + "-"*50)
    print(f"{'JOGO DA FORCA':^50}")
    print("-"*50)
    print(f"\nDificuldade: {nivel}")
    print(f"Palavra com {len(palavra)} letras!\n")
    print(f"Chances Restantes: {chances}")
    print("Tentativas:")
    print(*letras_usadas)


def jogar_rodada(palavra:str, chances:int):
    """Inicia nova rodada

    > Argumentos:
        - palavra (str): Palavra a ser descoberta pela usuário;
        - chances (int): Número máximo de tentativas.
    
    > Output:
        - Sem output.
    """
    # Declara lista vazia para armazenar letras já utilizadas
    letras_usadas = []
    
    # Gera rodadas consecutivas até que usuario ganhe ou fique sem chances
    while True:

        # Limpa tela e apresenta resumo da rodada
        apresenta_resumo(palavra, letras_usadas, chances)

        # Apresenta em tela letras já "descobertas"
        tentativa_palavra = atualiza_palavra(letras_usadas, palavra)
        print("\n" + tentativa_palavra + "\n")

        # Capta nova letra digitda pelo usuario
        chute = ler_letra(letras_usadas)

        # Adiciona letra a lista de letras ja utilizadas
        letras_usadas.append(chute)

        # Desconta chance se letra não estiver na palavra
        if chute not in palavra:
            chances -= 1

        # Atualiza partes já descobertas da palavra
        tentativa_palavra = atualiza_palavra(letras_usadas, palavra)

        # Limpa tela e apresenta resumo da rodada
        apresenta_resumo(palavra, letras_usadas, chances)

        # Apresenta em tela letras já "descobertas"
        tentativa_palavra = atualiza_palavra(letras_usadas, palavra)
        print("\n" + tentativa_palavra)

        # Verifica se jogo terminou
        if verifica_fim_jogo(tentativa_palavra, palavra, chances):
            break


def ler_opcao(opcoes_menu:list, txt:str):
    """Ler opcao do Menu

    > Argumentos:
        - opcoes_menu (list): Opções do menu
        - txt (str): Texto a ser apresentado no momento da leitura
    
    > Output:
        - (int): Opcao do menu indicada pelo usuario
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
            sys.exit("\n\nSaindo do jogo, até logo!...\n")
        
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


def selecionar_dificuldade():
    """Seleciona dificuldade do jogo

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Indica que variavel nivel tem escopo global
    global nivel

    # Niveis de dificuldade disponiveis
    opcoes_dificuldade = [
        "Fácil",
        "Difícil",
        "Aleatório",
    ]

    # Apresenta opcoes e capta escolha do usuario 
    print("--"*20)
    print("\n> Selecione a dificuldade:\n")
    for pos, dif in enumerate(opcoes_dificuldade):
        print(f"[{pos+1}] {dif}")
    opcao = ler_opcao(opcoes_dificuldade, "\nSelecione a dificuldade: ")

    # Ajusta configuracao de dificuldade
    nivel = opcoes_dificuldade[opcao-1]


def apresentar_menu(opcoes_menu:list):
    """Apresenta Menu Principal na tela

    > Argumentos:
        - opcoes_menu (list): Lista contendo opções do menu.
    
    > Output>
        - Sem output.
    """
    # Apresenta opcoes do menu 
    print("\n" + "=-"*25)
    print(f"\n{' BEM-VINDO AO JOGO DA FORCA 1.0! ':^50}\n")
    print("=-"*25)
    print("\n> Menu Principal:\n")
    for pos, opcao in enumerate(opcoes_menu):
        print(f"[{pos+1}] {opcao}")


def main():
    """Jogo da Forca

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    while True:

        # Lista de opcoes do menu
        opcoes_menu = [
            "Jogar",
            f"Selecionar a dificuldade (atual = {nivel})",
            "Sair do sistema",
            ]
        
        # Apresentar menu e captar opcao do usuario
        apresentar_menu(opcoes_menu)
        opcao = ler_opcao(opcoes_menu, "\nDigite um opção: ")

        # Joga nova rodada
        if opcao == 1:
            # Leitura da palavra e numero de chances
            palavra, chances = carrega_config(nivel)
            
            # Inicia nova rodada do jogo da forca
            jogar_rodada(palavra, chances)

        # Seleciona dificuldade do jogo
        elif opcao == 2:
            selecionar_dificuldade()
            limpar_tela()

        # Sai do jogo
        elif opcao == 3:
            sys.exit("\nSaindo do jogo, até logo!...\n")


if __name__ == "__main__":
    main()
