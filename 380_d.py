import math

S = str(input())
N = len(S)
Q = int(input())
K = list(map(int,input().split()))

ans = ["" for _ in range(Q)]
for i in range(Q):
    B = (K[i]-1) // N
    t = 0
    for j in range(100):
        if (B >> j) & 1:
            t += 1
    if t % 2 == 0:
        ans[i] = S[(K[i]-1) % N]
    else:
        ans[i] = S[(K[i]-1) % N].swapcase()

print(*ans)