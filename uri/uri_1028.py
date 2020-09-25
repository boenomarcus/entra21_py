# Numero de casos de teste
N = int(input())
casos = []
for i in range(N):
    casos.append(input())

# Calculando numero de pilhas por meio do MMC do algoritmo de Euclides
for caso in casos:
    a, b = map(int, caso.split())
    rst = 1
    while rst is not 0:
        rst = a%b
        a = b
        b = rst
    print(a)