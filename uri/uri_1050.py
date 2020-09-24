# Captando codigo DDD
ddd = int(input())

# Dados base
ddd_list = [
    [61, 71, 11, 21, 32, 19, 27, 31,],
    [
        "Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora",
        "Campinas", "Vitoria", "Belo Horizonte"
        ]
    ]

# Retorna cidade se DDD cadastrado
if ddd not in ddd_list[0]:
    print("DDD nao cadastrado")
else:
    print(ddd_list[1][ddd_list[0].index(ddd)])
