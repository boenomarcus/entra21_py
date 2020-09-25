# Captando valores nao-nulos
lst = []
n = 6
while n > 0:
    num = float(input())
    if num != 0:
        if num > 0:
            lst.append(num)
        n -= 1

# Apresentado numero de valores positivos
print(f"{len(lst)} valores positivos")
print(f"{sum(lst)/len(lst):.1f}")