N = int(input())
h = N//3600
N -= h*3600
m = N//60
s = N - m*60
print(f"{h}:{m}:{s}")