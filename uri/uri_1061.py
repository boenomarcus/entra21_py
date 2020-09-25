# Captando info de inicio e final do evento
di = int(input().split()[-1])
hi, mi, si = [int(x) for x in input().split()[::2]]
df = int(input().split()[-1])
hf, mf, sf = [int(x) for x in input().split()[::2]]

# Calculando tempo do evento
diff_days = df - di

# Calculando tempo transcorrido
if diff_days == 0:
    
    # Calculando diferenca de tempo
    diff_time = (hf*3600 + mf*60 + sf) - (hi*3600 + mi*60 + si)

    # Calculando horas, minutos, segundos
    h = diff_time//3600
    m = (diff_time%3600)//60
    s = (diff_time%3600)%60 

else:
    
    # Calculando diferenca de tempo
    diff_time = 24*3600 - (hi*3600 + mi*60 + si) + (hf*3600 + mf*60 + sf)

    # Calculando horas, minutos, segundos
    h = diff_time//3600
    m = (diff_time%3600)//60
    s = (diff_time%3600)%60

    # Corrigindo horas e numero de dias
    if h == 24:
        h = 0
    else:
        diff_days -= 1

# Apresentando resultados
print(f"{diff_days} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")