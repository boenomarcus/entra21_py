# Captando operacoes a serem executadas
n_casos = int(input())
operacoes = []
for i in range(n_casos):
    operacoes.append(input())

# Iterando sobre operacoes
for i in range(n_casos):

    # Lista de valores e operadores
    lst = operacoes[i].split()

    # Captando numeradores e denominadores
    N1, D1, N2, D2 = [int(x) for x in lst[::2]]

    # Captando operador matematico
    op = lst[3]

    # Realizando operacao indicada
    if op == "-":
        n_res, d_res = (N1*D2 - N2*D1), (D1*D2)
    elif op == "+":
        n_res, d_res = (N1*D2 + N2*D1), (D1*D2)
    elif op == "*":
        n_res, d_res = (N1*N2), (D1*D2)
    elif op == "/":
        n_res, d_res = (N1*D2), (N2*D1)

    # Calculando o MMC por meio do algoritmo de Euclides
    a, b = n_res, d_res
    rst = 1
    while rst is not 0:
        rst = a%b
        a = b
        b = rst
    mmc = a
    
    # Apresentando resultados
    print(f"{n_res}/{d_res} = {int(n_res/mmc)}/{int(d_res/mmc)}")



