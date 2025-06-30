import sys
sys.setrecursionlimit(10 ** 6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

N, Q = map(int,input().split())
X = list(map(int,input().split()))
G = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

def make_newls(array_1, array_2):
    sum_array = sorted(array_1 + array_2, reverse=True)
    length = min(20, len(sum_array))
    new_array = sum_array[:length]
    return new_array

max_nums = [[X[i]] for i in range(N)]

def dfs(p, x):
    for y in G[x]:
        if y != p:
            dfs(x, y)
            max_nums[x] = make_newls(max_nums[x], max_nums[y])

dfs(-1, 0)

# for i in range(N):
#     print(max_nums[i])

for _ in range(Q):
    v, k = map(int,input().split())
    print(max_nums[v-1][k-1])