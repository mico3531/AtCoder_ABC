import math

N, K = map(int,input().split())
A = list(map(int,input().split()))
M = max(A)

S = [0 for _ in range(M+1)]
for i in range(N):
    S[A[i]] += 1

T = [0 for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, (M // i) + 1):
        T[i] += S[i*j]

U = [0 for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, (M // i) + 1):
        if T[j] >= K:
            U[i*j] = max(U[i*j], j)

# print(S)
# print(T)
# print(U)

for i in range(N):
    print(U[A[i]])