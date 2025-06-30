N, M = map(int,input().split())

D = [1 for _ in range(M+1)]

for i in range(N):
    l, r = map(int,input().split())
    D[r] = max(l+1, D[r])

for i in range(2, M+1):
    D[i] = max(D[i], D[i-1])

ans = 0
for i in range(1, M+1):
    ans += (i-D[i]+1)

print(ans)