import math

S = str(input())
N = len(S)
T = 10 ** 100
t = math.ceil(math.log(T))

dp = [[0 for _ in range(N)] for _ in range(t)]

for i in range(N):
    if S[i] == "L":
        dp[0][i] = i-1
    else:
        dp[0][i] = i+1

for j in range(1, t):
    for i in range(N):
        k = dp[j-1][i]
        dp[j][i] = dp[j-1][k]

ans = [0 for _ in range(N)]
for i in range(N):
    for j in range(t):
        if (T >> j) & 1:
            i = dp[j][i]
    ans[i] += 1

print(*ans)