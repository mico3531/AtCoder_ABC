N = int(input())
G = [set() for _ in range(N)]
for _ in range(N-1):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    G[v].add(u)

dim = [len(G[i]) for i in range(N)]
# print(dim)

Ls = [ [ 0 for _ in range(dim[i]) ] for i in range(N) ]

M = 0
for i in range(N):
    k = 0
    for y in G[i]:
        Ls[i][k] = dim[y]
        k += 1

    Ls[i].sort(reverse = True)

    for k in range(dim[i]):
        Ls[i][k] *= (k+1)
    
    for k in range(dim[i]):
        M = max(M, Ls[i][k])

print(N - M - 1)