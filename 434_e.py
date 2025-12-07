import sys
sys.setrecursionlimit(10**7)

import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")

import bisect

N = int(input())

num_set = set()
X = [0 for _ in range(N)]
R = [0 for _ in range(N)]
for i in range(N):
    X[i], R[i] = map(int, input().split())
    num_set.add(X[i] + R[i])
    num_set.add(X[i] - R[i])

num_ls = list(num_set)
num_ls.sort()

G = [[] for _ in range(len(num_ls))]

for i in range(N):
    l_num = X[i] - R[i]
    r_num = X[i] + R[i]
    l_ind = bisect.bisect_left(num_ls, l_num)
    r_ind = bisect.bisect_left(num_ls, r_num)
    G[l_ind].append(r_ind)
    G[r_ind].append(l_ind)

# print(num_ls)
# print(G)

visited = [False for _ in range(len(num_ls))]

def dfs(p, x):
    visited[x] = True
    ret = True
    for y in G[x]:
        if y != p:
            if not visited[y]:
                bool_data = dfs(x, y)
                ret = ret and bool_data
            else:
                ret = False
    return ret

ans = len(num_ls)
for x in range(len(num_ls)):
    if not visited[x]:
        is_tree = dfs(-1, x)
        if is_tree:
            ans -= 1

print(ans)