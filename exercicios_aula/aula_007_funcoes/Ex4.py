#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

# Funcao para imprimir cabecalho
def imprime_cabecalho(empresa, caracter):
    msg = f"Funcionários {empresa} - 2020"
    print("\n" + caracter*50)
    print("{:^50}".format(msg))
    print(caracter*50 + "\n")

# Funcao para imprimir rodape
def imprime_rodape(caracter):
    print("\n" + caracter*50 + "\n")

# Declara empresa e caraceter desejado pro cabecalho/rodape
empresa = "olist"
caracter = "*"

# Apresenta cabecalho e rodape
imprime_cabecalho(empresa, caracter)
imprime_rodape(caracter)