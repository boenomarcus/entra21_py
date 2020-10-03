# Capta limites da soma
X = int(input())
Y = int(input())

# Ordena valores como X sendo menor e Y maior
maior = (X+Y+abs(X-Y))/2
if X == maior:
    X, Y = Y, X

# Itera sobre valores inteiros entre X e Y
soma = 0
for i in range(X, Y+1):
    if i%13 != 0:
        soma += i

# Apresenta resultado
print(soma)