import math

N, M = map(int,input().split())

ans = 1
for d1 in range(1, math.ceil(math.sqrt(M))+1):
    if M % d1 == 0:
        d2 = M // d1
        if M >= N * d1:
            ans = max(ans, d1)
        if M >= N * d2:
            ans = max(ans, d2)

print(ans)