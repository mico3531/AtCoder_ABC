import math

N = int(input())

T = [0 for _ in range(N)]
for i in range(N):
    T[i] = int(input())

ans = T[0]

for i in range(N):
    ans = math.lcm(ans, T[i])

print(ans)