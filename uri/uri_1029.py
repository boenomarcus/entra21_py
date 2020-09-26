# Numero de casos de teste
N = int(input())
casos = []
for i in range(N):
    casos.append(int(input()))

# Calcula fibonacci
for caso in casos:
    for i in range(caso+2):
        if i == 0:
            fib = [0]
        elif i == 1:
            fib.append(i)
        else:
            fib.append(fib[i-1] + fib[i-2])
    
    # Apresentando resultados
    print(f"fib({caso}) = {2*fib[caso+1]-2} calls = {fib[caso]}")