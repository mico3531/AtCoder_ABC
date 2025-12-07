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

UF = UnionFind(N)

B_count = [0 for _ in range(N)]
W_count = [1 for _ in range(N)]
is_W = [True for _ in range(N)]

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        u = Query[1] - 1
        v = Query[2] - 1
        if not UF.same(u, v):
            r_u = UF.find(u)
            r_v = UF.find(v)
            UF.union(u, v)
            r_w = UF.find(u)
            B_count[r_w] = B_count[r_u] + B_count[r_v]
            W_count[r_w] = W_count[r_u] + W_count[r_v]

    elif Query[0] == 2:
        v = Query[1] - 1
        r_v = UF.find(v)
        if is_W[v]:
            is_W[v] = False
            B_count[r_v] += 1
            W_count[r_v] -= 1
        else:
            is_W[v] = True
            B_count[r_v] -= 1
            W_count[r_v] += 1
            
    else:
        v = Query[1] - 1
        r_v = UF.find(v)
        if B_count[r_v] > 0:
            print("Yes")
        else:
            print("No")