# Capta denominador para calcula de resto
N = int(input())

# Iterando sobre casos
for i in range(1, 10000):
    if i%N == 2:
        print(i)