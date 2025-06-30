import math

N, M, K = map(int,input().split())

LCM = math.lcm(N, M)

L = 0
R = 2 * (10 ** 18)

while R - L >= 2:
    mid = (L+R) // 2
    count = (mid // N) + (mid // M) - 2 * (mid // LCM)
    if count >= K:
        R = mid
    else:
        L = mid
print(R)