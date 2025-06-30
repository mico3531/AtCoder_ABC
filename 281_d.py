N, K, D = map(int,input().split())
A = list(map(int,input().split()))

DP = [[-1 for _ in range(D)] for _ in range(K+1)]
for i in range(N):
    for j in range(K-1, -1, -1):
        for t in range(D):
            if DP[j][t] != -1:
                next = (t + A[i]) % D
                DP[j+1][next] = max(DP[j][t] + A[i], DP[j+1][next])
    DP[1][A[i] % D] = max(DP[1][A[i] % D], A[i])

if DP[-1][0] == -1:
    print(-1)
else:
    print(DP[-1][0])