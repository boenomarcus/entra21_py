# Captando input do usuario
n1, n2, n3, n4 = [round(float(x), 1) for x in input().split()]

# Calculando e apresentacao da media
avg = round((n1*2 + n2*3 + n3*4 + n4*1)/10, 1)
print(f"Media: {avg}")

# Detecta condicao de aprovacao/reprovacao do aluno
if avg < 5.0:
    print("Aluno reprovado.")
elif avg < 7.0:
    print("Aluno em exame.")
    
    # Deteca resultado do exame
    exam = round(float(input()), 1)
    print(f"Nota do exame: {exam}")
    new_avg = round((avg + exam)/2, 1)
    if new_avg >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {new_avg}")

elif avg >= 7.0:
    print("Aluno aprovado.")
