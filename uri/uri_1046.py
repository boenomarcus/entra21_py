# Captando inicio e fim do fogo
beg, end = map(int, input().split())

# Testando cenarios
if beg == end:
    print("O JOGO DUROU 24 HORA(S)")
elif beg > end:
    print(f"O JOGO DUROU {24-beg+end} HORA(S)")
else:
    print(f"O JOGO DUROU {end-beg} HORA(S)")