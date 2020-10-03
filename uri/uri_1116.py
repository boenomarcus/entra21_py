# Numero de casos
N = int(input())

# Capta casos e apresenta resultados
for i in range(N):
    
    # Capta numerador e denominador
    n, d = [int(x) for x in input().split()]

    # Apresenta resultados
    if d == 0:
        print("divisao impossivel")
    else:
        print(f"{n/d:.1f}")