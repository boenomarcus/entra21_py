# Captando salario
sal = round(float(input()), 2)

# Declara reajuste de acordo com faixa salarial
if sal <= 400:
    reajuste = 0.15
elif sal <= 800:
    reajuste = 0.12
elif sal <= 1200:
    reajuste = 0.1
elif sal <= 2000:
    reajuste = 0.07
else:
    reajuste = 0.04

# Apresentando resultados
print(f"Novo salario: {sal*(1+reajuste):.2f}")
print(f"Reajuste ganho: {sal*reajuste:.2f}")
print(f"Em percentual: {int(reajuste*100)} %")