# Numero de casos de teste
N = int(input())
casos = []
for i in range(N):
    casos.append(input())

# Declara quantidade de leds por numenro
leds_per_num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6,]

# Calcula numero de leds e apresenta resultados
for caso in casos:
    leds = 0
    for letra in caso:
        leds += leds_per_num[int(letra)]
    print(f"{leds} leds")