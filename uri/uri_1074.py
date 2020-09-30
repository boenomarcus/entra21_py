# Capta numero de casos
N = int(input())

# Iterando sobre casos
for i in range(N):
    num = int(input())
    if num == 0:
        # Apresenta resultado
        print("NULL")
    else:
        msg = ""
        if num%2 == 0:
            msg += "EVEN "
        else:
            msg += "ODD "
        if num > 0:
            msg += "POSITIVE"
        else:
            msg += "NEGATIVE"
        
        # Apresenta resultado
        print(msg)