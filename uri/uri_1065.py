# Captando valores nao-nulos
pares = 0
for i in range(5):
    num = int(input())
    if num%2 == 0:
        pares += 1

# Apresentado numero de valores positivos
print(f"{pares} valores pares")