import math

N, X = map(int,input().split())
x = list(map(int,input().split()))

Dist = []

for i in range(N):
    if x[i] != X:
        Dist.append(abs(x[i]-X))

if len(Dist) == 1:
    ans = Dist[0]
else:
    ans = math.gcd(Dist[0], Dist[1])
    for i in range(len(Dist)):
        ans = math.gcd(ans, Dist[i])

print(ans)