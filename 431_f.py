N, D = map(int, input().split())
A = list(map(int, input().split()))

mod = 998244353

count = [0 for _ in range(1 + 10**6)]
for i in range(N):
    count[A[i]] += 1

count_sum = [0 for _ in range(1 + 10**6)]
for num in range(1, 1 + 10**6):
    count_sum[num] = count_sum[num - 1] + count[num]

# print(count[:10])
# print(count_sum[:10])

fact = [1 for _ in range(1 + 10 ** 6)]
fact_rec = [1 for _ in range(1 + 10 ** 6)]

for i in range(1, 1 + 10 ** 6):
    fact[i] = fact[i-1] * i
    fact[i] %= mod

fact_rec[10 ** 6] = pow(fact[10 ** 6], -1, mod)
for i in range(10 ** 6 - 1, -1, -1):
    fact_rec[i] = fact_rec[i+1] * (i+1)
    fact_rec[i] %= mod

# print(fact[:10])
# print(fact_rec[:10])

ans = 1
for num in range(10 ** 6):
    if count[num] != 0:
        if num <= D:
            x = count_sum[num-1] + 1
            y = count[num]
        else:
            x = count_sum[num-1] - count_sum[num-D-1] + 1
            y = count[num]
        # print(num, x, y)
        pat = fact[x + y - 1] * fact_rec[x-1] * fact_rec[y]
        ans *= pat
        ans %= mod
        # print(ans)

print(ans)