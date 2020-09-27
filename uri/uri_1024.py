# Numero de casos de teste
N = int(input())
casos = []
for i in range(N):
    casos.append(input())

# Declara constantes
UPPER_ASCII_CODES = range(65, 91)
LOWER_ASCII_CODES = range(97, 123)

# Realizacao criptografia
for caso in casos:
    
    # Primeira rodada
    caso_update = ""
    for letra in caso:
        cod_ascii = ord(letra) 
        if cod_ascii in UPPER_ASCII_CODES or cod_ascii in LOWER_ASCII_CODES:
            caso_update += chr(cod_ascii+3)
        else:
            caso_update += letra
    
    # Segunda rodada
    caso_update = caso_update[::-1]
    
    # Terceira rodada
    beg = int(len(caso_update)/2)
    final = caso_update[:beg]
    for letra in caso_update[beg:]:
        final += chr(ord(letra)-1)
    
    # Apresenta string final
    print(final)