# Captando valores nao-nulos
pr, ip, ps, ns  = 0, 0, 0, 0
for i in range(5):
    num = int(input())
    
    # Testa se par ou impar
    if num%2 == 0:
        pr += 1
    else:
        ip += 1
    
    # Testa se positivo ou negativo
    if num > 0:
        ps += 1
    elif num < 0:
        ns += 1

# Apresentado numero de valores positivos
print(f"{pr} valor(es) par(es)")
print(f"{ip} valor(es) impar(es)")
print(f"{ps} valor(es) positivo(s)")
print(f"{ns} valor(es) negativo(s)")