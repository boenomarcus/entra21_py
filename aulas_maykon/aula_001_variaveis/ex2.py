#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

print("\n" + "=-"*30 + "\n")

# Definindo opcoes do menu
opcoes = [
    "Cadastrar funcionário",
    "Listar funcionários",
    "Editar funcionário",
    "Deletar funcionário",
    "Sair",
]

# Apresentado Menu
print("*"*30)
print("{:^30}".format("CADASTRO DE FUNCIONARIOS"))
print("*"*30 + "\n"*3)
for i, opcao in enumerate(opcoes):
    print("[{}] {}".format(i+1, opcao))
print("\n"*3 + "*"*30)

# Capta opcao do usuario
opcao = int(input("Digite uma opcao: "))

# Apresentando info baseada na opcao do usuario
if opcao == 1:
    print("\nCadastrando novo funcionário ...")
elif opcao == 2:
    print("\nListando funcionários cadastrados ...")
elif opcao == 3:
    print("\nEditando cadastro de funcionário ...")
elif opcao == 4:
    print("\nDeletando funcionário ...")
elif opcao == 5:
    print("\nSaindo, até logo ...")
else:
    print("\nOpção Inválida!")

print("\n" + "=-"*30 + "\n")