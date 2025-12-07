from atcoder import maxflow
import bisect

N = int(input())

X = [0 for _ in range(N)]
R = [0 for _ in range(N)]

num_set = set()

for i in range(N):
    line = list(map(int, input().split()))
    X[i] = line[0]
    R[i] = line[1]
    
    num_set.add(X[i] - R[i])
    num_set.add(X[i] + R[i])

num_ls = list(num_set)
num_ls.sort()
size = len(num_ls)

G = maxflow.MFGraph(N + size + 2)

for i in range(N):
    G.add_edge(N + size, i, 1)

    l_ind = bisect.bisect_left(num_ls, X[i] - R[i])
    r_ind = bisect.bisect_left(num_ls, X[i] + R[i])
    G.add_edge(i, N + l_ind, 1)
    G.add_edge(i, N + r_ind, 1)

for j in range(size):
    G.add_edge(N + j, N + size + 1, 1)

ans = G.flow(N + size, N + size + 1)

print(ans)