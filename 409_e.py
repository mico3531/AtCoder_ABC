import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
X = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u-1].append([v-1, w])
    G[v-1].append([u-1, w])

Energy = [0 for _ in range(N)]
def dfs(p, x, w_0):
    for Next in G[x]:
        y = Next[0]
        w = Next[1]
        if y != p:
            dfs(x, y, w)
    
    # print((p, x, w_0))
    Energy[p] += Energy[x] + w_0 * abs(X[x])
    X[p] += X[x]
    # print("E:", Energy)
    # print("X:", X)

dfs(-1, 0, 0)
print(Energy[0])