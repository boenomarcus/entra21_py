# Senha padrao
SENHA = "2002"

# Validacao de senha
while True:
    pwd = input()
    if pwd == SENHA:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")