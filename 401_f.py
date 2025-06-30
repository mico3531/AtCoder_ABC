from collections import deque

def dfs(G, x, Dist):
    for y in G[x]:
        if Dist[y] == -1:
            Dist[y] = Dist[x] + 1
            dfs(G, y, Dist)

def bfs(G, start):
    N = len(G)
    Dist = [-1 for _ in range(N)]
    Dist[start] = 0
    Queue = deque([start])

    while len(Queue) > 0:
        x = Queue.popleft()
        for y in G[x]:
            if Dist[y] == -1:
                Dist[y] = Dist[x] + 1
                Queue.append(y)
        
    return Dist

def make_dist(G):
    
    Dist_1 = bfs(G, 0)
    max_dist_1 = 0
    max_ind_1 = 0
    for i in range(len(G)):
        if Dist_1[i] > max_dist_1:
            max_ind_1 = i
            max_dist_1 = Dist_1[i]
    
    Dist_2 = bfs(G, max_ind_1)
    max_dist_2 = 0
    max_ind_2 = 0
    for i in range(len(G)):
        if Dist_2[i] > max_dist_2:
            max_ind_2 = i
            max_dist_2 = Dist_2[i]
    diam = max_dist_2

    Dist_3 = bfs(G, max_ind_2)
    
    ret = [max(Dist_2[i], Dist_3[i]) for i in range(len(G))]
    return diam, ret

N_1 = int(input())
G_1 = [[] for _ in range(N_1)]
for _ in range(N_1 - 1):
    u, v = map(int,input().split())
    G_1[u-1].append(v-1)
    G_1[v-1].append(u-1)

N_2 = int(input())
G_2 = [[] for _ in range(N_2)]
for _ in range(N_2 - 1):
    u, v = map(int,input().split())
    G_2[u-1].append(v-1)
    G_2[v-1].append(u-1)

diam_1, Dist_1 = make_dist(G_1)
diam_2, Dist_2 = make_dist(G_2)

diam = max(diam_1, diam_2)
Dist_1.sort()
Dist_2.sort()
# print(Dist_1)
# print(Dist_2)
# print(diam)

pre_sum = [0 for _ in range(N_2)]
pre_sum[N_2 - 1] = Dist_2[N_2 - 1]
if N_2 >= 2:
    for j in range(N_2 - 2, -1, -1):
        pre_sum[j] = pre_sum[j+1] + Dist_2[j]

j = N_2
ans = 0
for i in range(N_1):
    while True:
        if j == 0:
            break
        if Dist_1[i] + Dist_2[j-1] + 1 >= diam:
            j -= 1
        else:
            break
    ans += diam * j
    ans += (N_2 - j) * (Dist_1[i]+1)
    if j != N_2:
        ans += pre_sum[j]
print(ans)