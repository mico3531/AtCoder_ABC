import copy

mod = 998244353
frac = [1 for _ in range(10 ** 6)]
frac_inv = [1 for _ in range(10 ** 6)]

for i in range(1, 10**6):
    frac[i] = frac[i-1] * i
    frac[i] %= mod

frac_inv[-1] = pow(frac[-1], -1, mod)
for i in range(10**6 -2, -1, -1):
    frac_inv[i] = frac_inv[i+1] * (i+1)
    frac_inv[i] %= mod

S = str(input())

N = len(S)
num_count = [0 for _ in range(10)]
before_count = [[0 for _ in range(10)] for _ in range(N)]

num_count[int(S[0])] += 1
before_count[0][int(S[0])] += 1

for i in range(1, N):
    before_count[i] = before_count[i-1].copy()
    before_count[i][int(S[i])] += 1
    num_count[int(S[i])] += 1

ans = 0
for i in range(N):
    # print(before_count[i])
    x = int(S[i])
    p = before_count[i][x] - 1
    if x < 9:
        y = x + 1
        q = num_count[y] - before_count[i][y]
        if p+q >= max(p+1, q-1):
            # print(p+q, p+1)
            ans += frac[p+q] * frac_inv[p+1] * frac_inv[q-1]
            ans %= mod
print(ans)