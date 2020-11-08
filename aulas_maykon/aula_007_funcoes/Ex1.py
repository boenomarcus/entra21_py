#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def imprime_cabecalho(texto):
    print("\n" + "-"*10, texto, "-"*10 + "\n")

empresa = "olist"
imprime_cabecalho(f"Lista de funcionários da {empresa} em 2020")