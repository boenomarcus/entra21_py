
# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 50, 2% de desconto
# se o valor for superior a 100, 5% de desconto
# se o valor for superior a 200, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

# Imports
import sys

# Apresentação
print("\n>>> Lista de Compras!")


def lerProduto() -> float:
    while True:
        # Realiza leitura
        try:
            produto = input("Nome do Produto: ")
        
        # Trata exceção de saida do sistema
        except KeyboardInterrupt:
            print("\nAté logo!...\n")
            sys.exit()
            
        else:
            # Realiza validacao do dominio e retorna valor se valido
            if produto == "":
                print("[ERRO] Nome em branco, digite novamente!")
            else:
                return produto


def lerValor() -> float:
    while True:
        # Realiza leitura
        try:
            valor = float(input("Valor (R$): "))
        
        # Trata exceção de saida do sistema
        except KeyboardInterrupt:
            print("\nAté logo!...\n")
            sys.exit()
            
        # Trata exceção de erro de tipo imputado pelo usuario
        except ValueError:
            print("[ERRO] Valor inválido, digite novamente!")
        
        else:
            # Realiza validacao do dominio e retorna valor se valido
            if valor < 0:
                print("[ERRO] Valor inválido, digite novamente!")
            else:
                return valor


# # Capta input do usuário
# prods = {}
# while True:
#     print("\n> Cadastro de novo produto:")

#     # Realiza leitura do nome do produto
#     prod = lerProduto()

#     # Testa se produto já está cadastrado
#     if prod in prods.keys():
#         print("Produto já cadastrado! ...")
#     else:
#         # Cadastra produto e seu respe
#         prods[prod] = lerValor()
    
#     # Verifica se o usuario deseja cadastrar novo produto
#     while True:
#         res = input("Cadastrar novo produto?! [(s)/n] ").strip().lower()
#         if res in "sn":
#             break
#         print("[ERRO] Digite 's' ou 'n'!")
    
#     if res == "n":
#         break

# Declara dicionario vazio
prods = {
    "Feijão": 15.90,
    "Arroz": 39.99,
    "Suco": 6.50,
    "Chá": 6.95,
    "Pão": 6.52,
    "Café": 9.98,
}

# Calcula valor total
total = sum(prods.values())

# Apresenta valor total e descontos quando aplicável
print(f"\nValor Total = R$ {total:.2f}")
if total <= 50:
    print("Nenhum desconto aplicado!\n")
elif total <= 100:
    print("Desconto de 2% aplicado!")
    print(f"Valor Final = R$ {total*0.98:.2f}\n")
elif total <= 200:
    print("Desconto de 5% aplicado!")
    print(f"Valor Final = R$ {total*0.95:.2f}\n")
else:
    print("Desconto de 10% aplicado!")
    print(f"Valor Final = R$ {total*0.9:.2f}\n")

# Dict comprehesion para ordenar as chaves do dicionario
prods = {x:y for x, y in sorted(prods.items())}

# Apresenta dicionario com as keys em ordem alfabetica
print(f"Dicionario com chaves em ordem alabetica:\n{prods}\n")

