# Capta numero de linhas para imprimir
N = int(input())

# Apresenta resultados
nums = [1, 2, 3,]
for i in range(N):
    for j in range(3):
        print(f"{nums[j]} ", end="")
        nums[j] += 4
    print("PUM")