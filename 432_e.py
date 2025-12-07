class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])
    
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1
    
    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

N, Q = map(int, input().split())
A = list(map(int, input().split()))

Ls = [[0, 0] for _ in range(10 ** 6)]
for i in range(N):
    Ls[A[i]][0] += 1
    Ls[A[i]][1] += A[i]

def op(P, Q):
    return([P[0] + Q[0], P[1] + Q[1]])

def e():
    return [0, 0]

ST = SegTree(op, e, 10 ** 6, Ls)

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        x = Query[1]
        y = Query[2]
        
        now_data = ST.get(A[x-1])
        s = now_data[0]
        t = now_data[1]
        ST.set(A[x-1], [s-1, t-A[x-1]])

        pre_add = ST.get(y)
        u = pre_add[0]
        v = pre_add[1]
        ST.set(y, [u+1, v+y])

        A[x-1] = y
    else:
        l = Query[1]
        r = Query[2]

        if r <= l:
            print(N * l)
        else:
            lefter = ST.prod(0, l)
            middle = ST.prod(l, r)
            righter = ST.prod(r, 10 ** 6)
            ans = l * lefter[0] + middle[1] + r * righter[0]
            print(ans)