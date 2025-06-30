import math

N, M = map(int,input().split())

if N >= M // 2:
    ans = M // 2
else:
    ans = math.floor(N * 0.5 + M * 0.25)

print(ans)