# Captando pares inteiros e apresentando soma
while True:

    # Capta inicio e fim da sequencia
    X, Y = [int(x) for x in input().split()]

    # Teste condicao para fim do programa
    if X == Y:
        break

    # Maior valor
    maior = (X+Y+abs(X-Y))/2

    # Apresenta resultado
    if maior == X:
        print("Decrescente")
    else:
        print("Crescente")