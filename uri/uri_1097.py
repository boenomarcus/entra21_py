j = [7, 6, 5]
for mult in range(1, 10, 2):
    for index in range(3):
        print(f"I={1*mult} J={j[index]}")
        j[index] += 2