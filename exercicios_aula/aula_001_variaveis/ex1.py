#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

print("\n" + "=-"*30 + "\n")

# Capta input
print(">>> Cadastrando Dados de um Funcionário:\n")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
cpf = input("CPF: ")
rg = input("RG: ")
salario = float(input("Salário (R$): "))

# Apresenta resultados
print("""
>>> Dados Registrados:

Nome: {}
Sobrenome: {}
CPF: {}
RG: {}
Salário: R$ {:.2f}
""".format(
    nome, sobrenome, cpf, rg, salario
    )
    )

print("=-"*30 +"\n")