N, M = map(int,input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append([v, w])
    G[v].append([u, w])

Ls = [set() for _ in range(N)]

Used = [False for _ in range(N)]

def dfs(x, score):
    global ans
    Used[x] = True
    if x == N-1:
        ans = min(score, ans)
    else:
        for Next in G[x]:
            y = Next[0]
            w = Next[1]
            score = score ^ w
            if not Used[y]:
                dfs(y, score)
            score = score ^ w
    Used[x] = False

ans = float("INF")
dfs(0, 0)
print(ans)