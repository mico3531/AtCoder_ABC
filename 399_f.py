import math

N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
mod = 998244353

T = [[pow(A[r], k, mod) for k in range(K+1)] for r in range(N+1)]
T[0][0] = 0

for r in range(1, N+1):
    for k in range(K+1):
        for m in range(k+1):
            diff = math.comb(k, m) * pow(A[r], m, mod) * T[r-1][k-m]
            # print(r, k, m, diff)
            T[r][k] += diff
            T[r][k] %= mod

# for r in range(N+1):
#     print(T[r])

ans = 0
for i in range(1, N+1):
    ans += T[i][K]
    ans %= mod

print(ans)