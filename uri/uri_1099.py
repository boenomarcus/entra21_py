# Numero de casos
N = int(input())

# Capta casos e apresenta resultados
for i in range(N):
    
    # Realiza soma
    soma = 0
    X, Y = sorted([int(x) for x in input().split()])
    for num in range(X+1, Y):
        if num % 2 != 0:
            soma += num
    
    # Apresenta resultado
    print(soma)