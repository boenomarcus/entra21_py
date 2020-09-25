# Captando entrada (valor inteiro)
N = int(input())

# Apresentando resultados
for i in range(1, N+1):
    if i%2 == 0:
        print(f"{i}^2 = {i**2}")