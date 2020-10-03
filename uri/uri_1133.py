# Capta limites da soma
X = int(input())
Y = int(input())

# Ordena valores como X sendo menor e Y maior
maior = (X+Y+abs(X-Y))/2
if X == maior:
    X, Y = Y, X

# Itera sobre valores inteiros entre X e Y
for i in range(X+1, Y):
    rst = i%5
    if rst == 2 or rst == 3:
        print(i)