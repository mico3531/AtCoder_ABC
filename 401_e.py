from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

Judge = [True for _ in range(N)]
UF = UnionFind(N)

for i in range(1, N):
    for j in G[i]:
        if j < i:
            UF.union(i, j)
    
    if UF.size(i) == i+1:
        Judge[i] = True
    else:
        Judge[i] = False

Ans = [0 for _ in range(N)]
Use = [True for _ in range(N)]
count = 0

for i in range(N):
    if Use[i] == False:
        Use[i] = True
        count -= 1
    
    for j in G[i]:
        if j > i:
            if Use[j] == True:
                Use[j] = False
                count += 1
    
    if Judge[i] == True:
        print(count)
    else:
        print(-1)