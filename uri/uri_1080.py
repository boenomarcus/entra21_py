# Leitura e processamento de valores
maior = 0
pos = 0
for i in range(100):
    num = int(input())
    if num > maior:
        maior = num
        pos = i+1

# Apresentando resultados
print(maior)
print(pos) 