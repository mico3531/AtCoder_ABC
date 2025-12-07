import sys
sys.setrecursionlimit(10**6)

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

for i in range(1, N+1):
    G[i].sort()

Ans = []

def dfs(p, x):
    Ans.append(x)
    for y in G[x]:
        if y != p:
            dfs(x, y)
            Ans.append(x)

dfs(-1, 1)
print(*Ans)