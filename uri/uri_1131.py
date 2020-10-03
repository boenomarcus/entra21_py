# Inicializa programa
v_gre, v_int, emp = 0, 0, 0
while True:

    # Define vencedor ou empate
    g_int, g_gre = [int(x) for x in input().split()]
    if g_gre == g_int:
        emp += 1
    elif g_gre > g_int:
        v_gre += 1
    else:
        v_int += 1

    # Aguarda input para novo calculo ou fim do programa
    while True:
        resp = int(input("Novo grenal (1-sim 2-nao)\n"))
        if resp in [1, 2]:
            break
    
    # Finaliza programa quando indicado pelo usuário
    if resp == 2:
        break

# Apresenta resultados
print(f"{v_gre+v_int+emp} grenais")
print(f"Inter:{v_int}")
print(f"Gremio:{v_gre}")
print(f"Empates:{emp}")
if v_gre == v_int:
    print("Nao houve vencedor")
elif v_gre > v_int:
    print("Gremio venceu mais")
else:
    print("Inter venceu mais")