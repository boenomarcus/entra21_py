#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

print("\n" + "=-"*30 + "\n")

print(f">>> Calcula da Média entre Três Valores:\n")

def leitura_floats():

    # Leitura de valores
    nums = []
    for i in range(3):
        nums.append(float(input(f"Digite um valor [{i+1}/3]: ")))
    
    # Retorna valores
    return nums

# Calcula da media
f1, f2, f3 = leitura_floats()
media = (f1 + f2 + f3)/3

print(f"\nA média de {f1}, {f2} e {f3} é igual a {media:.2f}")

print("\n" + "=-"*30 + "\n")