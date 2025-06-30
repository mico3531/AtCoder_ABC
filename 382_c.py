N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

K = 2 * (10 ** 5)
F = [-1 for _ in range(K+1)]

i = 0
j = K
while i < N:
    if A[i] <= j:
        F[j] = i+1
        j -= 1
    else:
        i += 1

# print(F[:10])
for b in B:
    print(F[b])