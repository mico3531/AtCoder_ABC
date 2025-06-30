A, B, C, D = map(int, input().split())

mod_num = 998244353
fact = [1 for _ in range(A+B+C+D)]
for i in range(1, A+B+C+D):
    fact[i] *= fact[i-1] * i
    fact[i] %= mod_num

fact_inv = [pow(fact[i] ,-1, mod_num) for i in range(A+B+C+D)]

def comb(x, y):
    ret = fact[x] * fact_inv[x-y] * fact_inv[y]
    return ret % mod_num

ans = 0
for x in range(B+1):
    count = comb(A-1+x, x)
    count *= comb(B+D+C-x, C)
    ans += count
    ans %= mod_num

print(ans)