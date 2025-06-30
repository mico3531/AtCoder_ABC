import math

N = int(input())
A = [0 for _ in range(5)]
for i in range(5):
    A[i] = int(input())

m = min(A)
G = math.ceil(N / m)
print(G+4)