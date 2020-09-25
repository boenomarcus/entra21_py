# Numero de casos de teste
N = int(input())
casos = []
for i in range(N):
    tmp = []
    for j in range(3):
        tmp.append(input())
    casos.append(tmp)

# Processando strings
for caso in casos:
    
    dieta = caso[0]
    cafe_manha = caso[1]
    almoco = caso[2]

    # Sem dieta
    if dieta == "":
        if cafe_manha != "" or almoco != "":
            print("CHEATER")
        else:
            print("")
    
    # Com dieta prescrita
    else:

        # Declara variavel para guardar msg
        msg = ""

        # Testando cafe_manha
        for letra in cafe_manha:
            if letra in dieta:
                dieta = dieta.replace(letra, "", 1)
            else:
                msg = "CHEATER"
        
        # Testanda almoco
        if msg != "CHEATER":
            for letra in almoco:
                if letra in dieta:
                    dieta = dieta.replace(letra, "", 1)
                else:
                    msg = "CHEATER"
        
        # Criando msg final
        if msg != "CHEATER":
            print("".join(sorted(dieta)))
        else:
            print(msg)