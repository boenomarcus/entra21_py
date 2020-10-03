# Inicializa programa
alc, gas, die = 0, 0, 0
while True:

    # Le tipo de combustivel
    resp = int(input(""))

    # Cadastra combustivel utilizado e apresenta resultados
    if resp == 1:
        alc += 1
    elif resp == 2:
        gas += 1
    elif resp == 3:
        die += 1
    elif resp == 4:
        print("MUITO OBRIGADO")
        print(f"Alcool: {alc}")
        print(f"Gasolina: {gas}")
        print(f"Diesel: {die}")
        break