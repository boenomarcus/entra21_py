# Iniciando programa
from bisect import bisect_left
caso = 0
while True:

    # Captando numero de marbles e queries
    N, Q = map(int, input().split())

    # Encerra tomada de dados se marbles e queries == 0
    if N == 0 and Q == 0:
        break

    # Registra dados
    caso += 1
    marbles = []
    print(f"CASE# {caso}:")
    for i in range(N+Q):
        if i < N:
            marbles.append(int(input()))
        if i == N:
            marbles.sort()
        if i >= N:
            q = int(input())
            pos = bisect_left(marbles, q)
            if pos < len(marbles) and marbles[pos] == q:
                    print(f"{q} found at {pos+1}")
            else:
                print(f"{q} not found")