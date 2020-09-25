# le salario do usuario
sal = round(float(input()), 2)

# Declara variavel para armezenar imposto
imposto = 0

# Imposto sobre valores maiores que R$ 4500
if sal//4500 >= 1:
    imposto += (sal-4500)*0.28
    sal = 4500

# Imposto sobre valores maiores que R$ 3000
if sal//3000 == 1:
    imposto += (sal-3000)*0.18
    sal = 3000

# Imposto sobre valores maiores que R$ 2000
if sal//2000 == 1:
    imposto += (sal-2000)*0.08

# Apresenta resultados
if imposto == 0:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")