# Captando pares inteiros e apresentando soma
while True:

    # Capta par de coordenadas
    X, Y = [int(x) for x in input().split()]

    # Testa condicao para fim do programa
    if X == 0 or Y == 0:
        break
    
    # Apresentando resultados
    if X > 0:
        if Y > 0:
            print("primeiro")
        else:
            print("quarto")
    else:
        if Y > 0:
            print("segundo")
        else:
            print("terceiro")