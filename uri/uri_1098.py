i, j = [0, 0, 0,], [10, 20, 30,]
while i[0] <= 20:
    for index in range(3):
        if i[index]%10 == 0:
            print(f"I={int(i[index]/10)} J={int(j[index]/10)}")
        else:
            print(f"I={i[index]/10:.1f} J={j[index]/10:.1f}")
        i[index] += 2
        j[index] += 2