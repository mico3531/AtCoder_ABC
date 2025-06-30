N = int(input())
S = str(input())

num = 10

Ls = [ord(S[i]) - ord("A") for i in range(N)]
DP = [[[0 for _ in range(num)] for _ in range(2**num)] for _ in range(N+1)]

mod = 998244353

for i in range(1, N+1):
    x = Ls[i-1]
    
    for j in range(2**num):
        for k in range(num):
            DP[i][j][k] = DP[i-1][j][k]
    
    for j in range(2**num):
        for k in range(num):
            if (j >> k) & 1:
                continue
            if (j >> x) & 1:
                continue
            if k == x:
                DP[i][j][x] += DP[i-1][j][x]
            else:
                DP[i][j+2**k][x] += DP[i-1][j][k]
    DP[i][0][x] += 1

ans = 0
for j in range(2**num):
    for k in range(num):
        ans += DP[N][j][k]
ans %= mod

# for i in range(N+1):
#     print(DP[i])

print(ans)