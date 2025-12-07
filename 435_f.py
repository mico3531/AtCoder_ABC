import sys
sys.setrecursionlimit(10**6)

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

from collections import deque

N = int(input())
P = list(map(int, input().split()))

for i in range(N):
    P[i] *= -1

Queue = deque([])
Queue.append([P[0], 0])

parent = [[] for _ in range(N)]
l_child = [[] for _ in range(N)]
r_child = [[] for _ in range(N)]

for i in range(1, N):
    check = True
    while check:
        if len(Queue) == 0:
            Queue.append([P[i], i])
            check = False
        else:
            last_data = Queue.pop()
            last_val = last_data[0]
            last_ind = last_data[1]
            if P[i] > last_val:
                parent[i] = [last_ind, abs(last_ind - i)]
                r_child[last_ind] = [i, abs(last_ind - i)]

                Queue.append([last_val, last_ind])
                Queue.append([P[i], i])
                check = False
            else:
                l_child[i] = [last_ind, abs(last_ind - i)]
                parent[last_ind] = [i, abs(last_ind - i)]
    # print(Queue)

# print("parent is", parent)
# print("r_child is", r_child)
# print("l_child is", l_child)

k = P.index(-N)

def dfs(i):
    if len(l_child[i]) == 0 and len(r_child[i]) == 0:
        return 0
    else:
        ret = 0
        if len(l_child[i]) != 0:
            x = l_child[i][0]
            d = l_child[i][1]
            ret = dfs(x) + d
        if len(r_child[i]) != 0:
            x = r_child[i][0]
            d = r_child[i][1]
            ret = max(ret, dfs(x) + d)
        return ret

print(dfs(k))