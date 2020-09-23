# Captando input do usuario
X, Y = map(int, input().split())

# Declarando info de valores
valores = [4.0, 4.5, 5.0, 2.0, 1.5,]

# Calculando resultado
total = valores[X-1]*Y

# Apresentando resultados
print(f"Total: R$ {total:.2f}")
