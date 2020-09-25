# Captando valor inteiro qualquer
X = int(input())

# Ajustando valor se par
if X%2 == 0:
    X += 1

# Apresentando valores impares
for i in range(6):
    print(X + i*2)