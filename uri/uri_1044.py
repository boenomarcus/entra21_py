# Captando possiveis multiplos
A, B = map(int, input().split())

# Encontrando maior valor
maiorAB = (A+B+abs(A-B))/2

# Verificando se sao multiplos
if maiorAB == A:
    if A%B == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if B%A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

