# Capta numero de casos de teste
N = int(input())

# Iterando sobre casos
for i in range(N):
    f1, f2, f3 = map(float, input().split())
    print(f"{(f1*2 + f2*3 + f3*5)/10:.1f}")