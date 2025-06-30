import math

N, K = map(int,input().split())

ans = 0
for i in range(1, N+1):
    if i >= K:
        ans += 1
    else:
        t = math.ceil(math.log(K / i, 2))
        ans += 2 ** (-t)

ans /= N

print(ans)