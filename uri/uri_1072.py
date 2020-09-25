# Captando valores inteiros
n = int(input())
inter_in = 0
inter_out = 0
for i in range(n):
    num = int(input())
    if 10 <= num <= 20:
        inter_in += 1
    else:
        inter_out += 1

# Apresentando resultados
print(f"{inter_in} in")
print(f"{inter_out} out")