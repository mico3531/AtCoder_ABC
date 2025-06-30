N, M = map(int,input().split())
p = 1000000007

A = [0 for _ in range(M)]
for j in range(M):
    A[j] = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = 1
j = 0
for i in range(1, N+1):
    if j < M:
        if A[j] != i:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            j += 1
    else:
        dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= p

print(dp[N])