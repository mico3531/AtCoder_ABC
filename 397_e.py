# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int,input().split())

G = [set() for _ in range(N*K)]
for _ in range(N*K - 1):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    G[v].add(u)

S = [1 for _ in range(N*K)]
C = [len(G[i]) - 1 for i in range(N*K)]
C[0] += 1

def dfs(x, p):
    for y in G[x]:
        if y != p:
            dfs(y, x)
            S[x] += S[y]
    
    # print(x, S, C)
    if S[x] < K:
        if C[x] >= 2:
            print("No")
            exit()
    elif S[x] > K:
        print("No")
        exit()
    else:
        if C[x] >= 3:
            print("No")
            exit()
        else:
            S[x] = 0
            C[p] -= 1

dfs(0, -1)
print("Yes")