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

N, Q = map(int, input().split())

X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
for i in range(N):
    X[i], Y[i] = list(map(int, input().split()))

UF = UnionFind(N)
for _ in range(Q):
    Query = list(map(int, input().split()))
    
    if Query[0] == 1:
        a = Query[1]
        b = Query[2]
        X.append(a)
        Y.append(b)
    
    elif Query[1] == 2:
        min_dist = float("INF")
        for i in range(N-1):
            for j in range(i+1, N):
                if not UF.same(i, j):
                    dist = abs(X[i] - X[j]) + abs(Y[i] - Y[j])
                    min_dist = min(min_dist, dist)