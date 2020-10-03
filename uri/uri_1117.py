# Capta notas
notas, media = 2, 0
while notas > 0:
    nota = float(input())
    if 0.0 <= nota <= 10.0:
        media += nota/2
        notas -= 1
    else:
        print("nota invalida")

# Apresenta media
print(f"media = {media:.2f}")