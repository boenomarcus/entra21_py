# Captando inicio e fim do fogo
beg_h, beg_m, end_h, end_m = map(int, input().split())

# Testando cenarios
if beg_h == end_h:

    if beg_m == end_m:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    
    elif beg_m > end_m:
        print(f"O JOGO DUROU 23 HORA(S) E {60-beg_m+end_m} MINUTO(S)")
    
    else:
        print(f"O JOGO DUROU 0 HORA(S) E {end_m-beg_m} MINUTO(S)")

elif beg_h > end_h:

    if beg_m == end_m:
        print(f"O JOGO DUROU {24-beg_h+end_h} HORA(S) E 0 MINUTO(S)")
    
    elif beg_m > end_m:
        hrs = 23-beg_h+end_h
        mins = 60-beg_m+end_m
        print(f"O JOGO DUROU {hrs} HORA(S) E {mins} MINUTO(S)")
    
    else:
        hrs = 24-beg_h+end_h
        mins = end_m-beg_m
        print(f"O JOGO DUROU {hrs} HORA(S) E {mins} MINUTO(S)")

else:
    if beg_m == end_m:
        print(f"O JOGO DUROU {end_h-beg_h} HORA(S) E 0 MINUTO(S)")
    
    elif beg_m > end_m:
        hrs = end_h-beg_h-1
        mins = 60-beg_m+end_m
        print(f"O JOGO DUROU {hrs} HORA(S) E {mins} MINUTO(S)")
    
    else:
        hrs = end_h-beg_h
        mins = end_m-beg_m
        print(f"O JOGO DUROU {hrs} HORA(S) E {mins} MINUTO(S)")