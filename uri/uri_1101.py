# Captando pares inteiros e apresentando soma
while True:

    # Capta inicio e fim da sequencia
    X, Y = sorted([int(x) for x in input().split()])
    
    # Testa condicao para fim do programa
    if X <= 0:
        break

    # Apresenta resultados
    seq = list(range(X, Y+1))
    for num in seq:
        print(f"{num} ", end="")
    print(f"Sum={sum(seq)}")