N, M = map(int,input().split())

G = [set() for _ in range(N+1)]
ans = 0
for _ in range(M):
    u, v = map(int,input().split())
    if u == v:
        ans += 1
    elif u in G[v]:
        ans += 1
    else:
        G[u].add(v)
        G[v].add(u)

print(ans)