# Capta numero de casos de teste
N = int(input())

# Declara dicionario para armazenar dados
dados = {
    "R": 0,
    "S": 0,
    "C": 0,
    "Total": 0
}

# Captando casos de teste
for i in range(N):
    q, t = input().split()
    dados[t] += int(q)
    dados['Total'] += int(q)

# Apresentando resultados
total = dados['Total']
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {dados['C']}")
print(f"Total de ratos: {dados['R']}")
print(f"Total de sapos: {dados['S']}")
print(f"Percentual de coelhos: {dados['C']*100/total:.2f} %")
print(f"Percentual de ratos: {dados['R']*100/total:.2f} %")
print(f"Percentual de sapos: {dados['S']*100/total:.2f} %")