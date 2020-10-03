# Capta numero de casos
N = int(input())

# Itera sobre casos
for caso in range(N):

    # Capta numero de pessoas e salto
    n, k = [int(x) for x in input().split()]

    # Cria lista base para detectar o sobrevivente
    people = list(range(1,n+1))

    # Encontra o sovrevivente
    p = 0
    while len(people) > 1:
        p += k-1
        while p >= len(people):
            p -= len(people)
        people.pop(p)
    
    # Apresenta sobrevivente
    print(f"Case {caso+1}: {people[0]}")