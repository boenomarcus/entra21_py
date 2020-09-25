# Captando dois valores inteiros
X, Y = sorted([int(input()), int(input())])

# Declarando variavel para armezenar soma dos impares
soma = 0

# Testando impares para soma
for i in range(X+1, Y):
    if i%2 != 0:
        soma += i

# Apresentando resultados
print(soma)