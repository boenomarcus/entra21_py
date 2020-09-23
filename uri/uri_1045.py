# Captando lados do possivel triangulo (com validacao simples)
valid_input = False
while valid_input is False:
    A, B, C = sorted(map(float, input().split()), reverse=True)
    if A > 0 and B > 0 and C > 0:
        valid_input = True

# Checando possiveis triangulos
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")