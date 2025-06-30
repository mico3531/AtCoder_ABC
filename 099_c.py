N = int(input())

Ls = [1]

s = 6
while s <= N:
    Ls.append(s)
    s *= 6

t = 9
while t <= N:
    Ls.append(t)
    t *= 9

DP = [N+1 for _ in range(N+1)]
DP[0] = 0
for i in range(N):
    for x in Ls:
        if i+x <= N:
            DP[i+x] = min(DP[i+x], DP[i]+1)

print(DP[N])