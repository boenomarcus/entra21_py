#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

# Define funcao para a divisao
def divisao(n1, n2):
    res = n1/n2
    return res

print("\n" + "=-"*30 + "\n")

# Capta valores digitados pelo usuário
print(">>> Razão entre dois valores\n")
n1 = float(input("Digite um valor [1/2]: "))
n2 = float(input("Digite um valor [2/2]: "))

# Realiza a divisao
res = divisao(n1, n2)

# Apresenta resultados
print(f"\nO razão entre {n1} e {n2} é igual a {res:.2f}")

print("\n" + "=-"*30 + "\n")