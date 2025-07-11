# Hopcroft-Karp Algorithm
from collections import deque
class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)
 
    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)
 
    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None
 
    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0
 
    def flow(self):
        flow = 0
        G = self.G
        bfs = self.bfs; dfs = self.dfs
        while bfs():
            *self.it, = map(iter, G)
            while dfs(0, 1):
                flow += 1
        return flow
 
    def matching(self):
        return [cap for _, cap, _ in self.backwards]

N = int(input())
S = [[] for _ in range(N)]
for i in range(N):
    S[i] = list(map(int, input().split()))
G = [[] for _ in range(N)]
for j in range(N):
    G[j] = list(map(int, input().split()))

Dist_sq = [
    [(S[i][0] - G[j][0]) ** 2 + (S[i][1] - G[j][1]) ** 2 for j in range(N)] 
    for i in range(N)]

# for i in range(N):
#     print(Dist[i])

def check(M):
    HK = HopcroftKarp(N, N)
    M_sq = M*M
    for i in range(N):
        for j in range(N):
            if Dist_sq[i][j] <= M_sq:
                HK.add_edge(i, j)
    return HK.flow() == N

epsilon = 1.0e-6
L = 1
R = 2 * (10**18)
M = (L+R) / 2
diff = (R-L) / M
while diff > epsilon:
    M = (L+R) / 2
    if check(M):
        R = M
    else:
        L = M
    diff = (R-L) / M

print("{:f}".format((L+R) / 2))