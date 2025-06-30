H, N = map(int,input().split())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for i in range(N):
    A[i], B[i] = map(int,input().split())

DP = [10 ** 10 for _ in range(H+1)]
DP[0] = 0
for j in range(H):
    for i in range(N):
        damage = A[i]
        cost = B[i]
        total = min(j + damage, H)
        DP[total] = min(DP[total], DP[j] + cost)

print(DP[-1])