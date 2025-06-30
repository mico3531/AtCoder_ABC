import sys
sys.setrecursionlimit(10**6)

import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int,input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    G[u-1].add(v-1)
    G[v-1].add(u-1)

Visited = [False for _ in range(N)]

def dfs(x):
    Visited[x] = True
    for y in G[x]:
        if not Visited[y]:
            dfs(y)

conn_num = 0
for i in range(N):
    if not Visited[i]:
        dfs(i)
        conn_num += 1

# print(conn_num)
ans = M - N + conn_num
print(ans)