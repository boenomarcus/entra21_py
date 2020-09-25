# Captando info de cidades, moradores e consumo
dados = {}
cidades = 0
while True:

    # Numero de imoveis
    N = int(input())
    if N == 0:
        break
    
    # Atualiza numero cidades
    cidades += 1

    # Cadastrando moradores e consumo
    m, c, cr = [], [], []
    for i in range(N):
        mi, ci = [int(x) for x in input().split()]
        m.append(mi)
        c.append(ci)
        cr.append(int(ci/mi))

    # Cria indice de consumos relativos
    indice = {}
    for i in list(set(cr)):
        indice[i] = 0
    for k, i in enumerate(cr):
        indice[i] += m[k]
    
    # Armazena na lista de dados
    city_id = str(cidades)
    dados[city_id] = {}
    dados[city_id]["imoveis"] = N
    dados[city_id]["moradores"] = m
    dados[city_id]["consumo"] = c
    dados[city_id]["consumo_rel"] = indice

# Apresentando resultados
for i in range(cidades):

    # ID cidade
    city_id = str(i+1)

    # consumos relativos
    crs = list(dados[city_id]["consumo_rel"].keys())
    mrs = list(dados[city_id]["consumo_rel"].values())
    cons_rel = " ".join([str(p)+"-"+str(c) for c, p in sorted(zip(crs, mrs))])

    # consumo medio
    cons = sum(dados[city_id]["consumo"])/sum(dados[city_id]["moradores"])

    # Apresentando resultados
    print(f"Cidade# {city_id}:")
    print(cons_rel)
    print(f"Consumo medio: {(int(cons*(10**2))/(10**2)):.2f} m3.")

    # Pulo linha se nova cidade
    if i+1 < cidades:
        print("")