#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

print("\n" + "=-"*30 + "\n")

# Funcao para calculo da raiz
def raiz(valor, indice):
    res = valor**(1/indice)
    return res

# Capta radicando e indice
print(">>> Cálculo da raiz de um valor: \n")
rad = float(input("Digite o radicando: "))
ind = int(input("Digite o índice: "))

# Calcula raiz e apresenta resultados
res = raiz(rad, ind)
print(f"\nA raiz de {rad}, com índice {ind}, é igual a {res:.2f}")

print("\n" + "=-"*30 + "\n")


