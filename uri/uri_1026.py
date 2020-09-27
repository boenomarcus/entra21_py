# Inicio loop para 
while True:

    # Captando numeros inteiros para soma
    try:
        nums = input()
    except EOFError:
        # Permite string vazia na entrada
        break

    # Se a entrada for vazia o programa é encerrado
    if nums == "":
        break

    # Declara numeros inteiros para soma Mofiz
    A, B = [abs(int(x)) for x in nums.split()]

    # Apresenta resultados
    print(A^B)

    # O código abaixo pode ser substituido pelo operador ^ que realizará
    # a operação "bitwise exclusive or"
    # (https://wiki.python.org/moin/BitwiseOperators)
    #
    # Dessa forma o bit no output será igual ao bit no primeiro byte se a
    # posição correspondente no segundo byte for igual a 1. No caso da posicao
    # no segundo byte ser igual a zero o bit no output assumirá o complementar
    # do bit no primeiro byte (zero se um ou um se zero).

    # Essa relacao pode ser feita neste caso pois as portas AND que são 
    # combinadas para formar a soma fazem o inverso do primeiro byte em um caso
    # e o inversor do segundo byte em outro caso. A combinação das saídas com 
    # uma porta OR gera a propriedade estabelecida pelo operador 
    # bitwise exclusive or
    
    # # Define maior e conta numero de bits "nao-nulos"
    # maiorAB = int((A+B+abs(A-B))/2)
    # num_bits = len(bin(maiorAB).split("b")[-1])

    # # Declara A e B com numero de bits do maior valor
    # A = bin(A).split("b")[-1].zfill(num_bits)
    # B = bin(B).split("b")[-1].zfill(num_bits)

    # # Cria lista com bits de mesmo posicao
    # bit_stream = [[int(a), int(b)] for a, b in zip(A, B)]

    # # Expressao
    # #    Mofiz Sum = (A AND NOT(B)) OR (NOT(A) AND B) 

    # # A AND NOT(B)
    # a_and_not_b = []
    # for bits in bit_stream:
    #     a_and_not_b.append(bits[0] and not bits[1])

    # # NOT(A) AND B
    # not_a_and_b = []
    # for bits in bit_stream:
    #     not_a_and_b.append(not bits[0] and bits[1])

    # # SUM (OR Port)
    # mofiz_sum = []
    # bit_stream = [[int(a), int(b)] for a, b in zip(a_and_not_b, not_a_and_b)]
    # for bits in bit_stream:
    #     mofiz_sum.append(bits[0] or bits[1])

    # # Apresentando resultados
    # print(int("".join([str(x) for x in mofiz_sum]), 2))