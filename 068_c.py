N, M = map(int,input().split())

G = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

ans = "IMPOSSIBLE"
for x in G[1]:
    if N in G[x]:
        ans = "POSSIBLE"
        break

print(ans)