"""
Jogo da Forca 1.0!

Blusoft/Senac - Formação em Python Entra21 2020

Autor: Bruno Sadoski
Revisado por: Marcus Moresco Boeno
Último update: 2020-11-06

"""

# Standard library imports
import os
import sys
import pathlib

# Define constantes
CONFIG_PATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    "config_forca.cfg"
    )

def carrega_config(config:str) -> list:
    """Carrega configurações para o jogo da forca

    > Argumentos:
        - config (str): Caminho para arquivo de configuração (cfg).
    
    > Output:
        - (list): Lista com palavra e numero de chances
    """
    with open(config, "r") as f:
        return [line.split(":")[-1].strip() for line in f.readlines()]


def ler_letra(letras_usadas:list) -> str:
    """Função para leitura e validação de letra

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
                print("[ERRO] Letra inválida, tente novamente!")
            
            # Checa se caracter é uma letra da tabela ASCII
            elif ord(letra) not in range(ord("a"), ord("z") + 1):
                print("[ERRO] Entrada inválida, digite uma letra!")
            
            # Checa se letra já foi utilizada
            elif letra in letras_usadas:
                print("[ERRO] Letra já utilizada, tente novamente!") 

            # Retorna letra se entrada for valida e ainda nao utilizada
            else:
                return letra

def limpar_tela():
    """Função para realizar a limpeza do terminal

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada rodada
    # "cls" para windows e "clear" para linux/mac (posix)
    os.system('cls') if os.name == 'nt' else os.system('clear')


def atualiza_palavra(letras_usadas:list) -> str:
    """Atualiza partes já descobertas da palavra

    > Argumentos:
        - letras_usadas (list): Lista indicando as letras já utilizadas.
    
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


def jogar_rodada(palavra:str, chances:int):
    """Inicia nova rodada do jogo da forca

    > Argumentos:
        - palavra (str): Palavra a ser descoberta pela usuário.
    
    > Output:
        - chances (int): Número máximo de tentativas
    """
    
    # Declara lista vazia para armazenar letras já utilizadas
    letras_usadas = []
    
    # Gera rodadas consecutivas até que usuario ganhe ou fique sem chances
    while True:

        # Limpa terminal antes de cada rodada
        limpar_tela()
                
        # Apresenta chance restantes e letras já utilizadas
        print(f"Número de chances: {chances} - tentativas:")
        print(*letras_usadas)

        # Apresenta em tela letras já "descobertas"
        tentativa_palavra = atualiza_palavra(letras_usadas)
        print("\n" + tentativa_palavra + "\n\n")

        # Capta nova letra digitda pelo usuario
        chute = ler_letra(letras_usadas)

        # Adiciona letra a lista de letras ja utilizadas
        letras_usadas.append(chute)

        # Atualiza partes já descobertas da palavra
        tentativa_palavra = atualiza_palavra(letras_usadas)

        # Palavra finalizada, usuario venceu!
        if tentativa_palavra == palavra:
            print(f"\nVocê ganhou restando {chances} tentativa(s)!\n")
            print(f"   > Palavra: {tentativa_palavra}\n")
            break

        # Palavra nao finalizada, reduza uma chance
        else:
            chances -= 1

            # Se acabaram as chances indica que o usuario perdeu
            if chances == 0:
                print("\nVocê perdeu!\n")
                break


def main():
    """Jogo da Forca

    Função para execução de sucessivas rodadas do jogo da forca

    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    while True:
        
        # Leitura da palavra e numero de chances a partir do arquivo config
        palavra, chances = carrega_config(CONFIG_PATH)
        
        # Inicia nova rodada do jogo da forca
        jogar_rodada(palavra, int(chances))

        # Verifica se o usuario deseja jogar novamente
        while True:
            
            # Realiza leitura da opcao do usuario
            try:
                res = input("Jogar nova rodada? [(s)/n] ").strip().lower()
            
            # Sai do jogo quando indicado pelo usuario
            except KeyboardInterrupt:
                print("\nSaindo do jogo, até logo!...\n")
                sys.exit()
            
            # Checa se entrada é valida
            else:

                # Se entrada for valida quebre o ciclo e confira a opcao
                if res in "sn":
                    break
                
                # Opcao invalida, pede nova entrada do usuario
                else:
                    print("[ERRO] Entrada inválida, digite 's' ou 'n'!")
        
        # Checa se usuário quer jogar novamente se nao sai do jogo
        if res == "n":
            print("\nSaindo do jogo, até logo!...\n")
            sys.exit()


if __name__ == "__main__":
    main()

    

