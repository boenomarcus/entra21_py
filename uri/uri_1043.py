# Captando lados do possivel triangulo
A, B, C = map(float, input().split())

# Condições para os valores digitados formarem um triângulo
cond_01 = A < B + C
cond_02 = B < A + C
cond_03 = C < A + B

# Apresentando resultados
if cond_01 and cond_02 and cond_03:
    print(f"Perimetro = {A+B+C:.1f}")
else:
    print(f"Area = {(A+B)*C/2:.1f}")