import math

A, B = map(int,input().split())

G = math.gcd(A, B)
N = 3 + math.ceil(math.sqrt(G))

p = 0

for i in range(2, N):
    if G % i == 0:
        p += 1
        while G % i == 0:
            G //= i
if G != 1:
    p += 1

print(p+1)