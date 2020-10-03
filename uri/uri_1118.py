# Inicializa programa
while True:

    # Capta notas
    notas, media = 2, 0
    while notas > 0:
        nota = float(input())
        if 0.0 <= nota <= 10.0:
            media += nota/2
            notas -= 1
        else:
            print("nota invalida")

    # Apresenta media
    print(f"media = {media:.2f}")

    # Aguarda input para novo calculo ou fim do programa
    while True:
        resp = int(input("novo calculo (1-sim 2-nao)\n"))
        if resp in [1, 2]:
            break
    
    # Finaliza programa quando indicado pelo usuário
    if resp == 2:
        break