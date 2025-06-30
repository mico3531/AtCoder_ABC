# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> tuple[list[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a: list[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def lt(self, x: T) -> T | None:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> T | None:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> T | None:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> T | None:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

N, M, S_X, S_Y = map(int,input().split())
Dic_X = dict()
Dic_Y = dict()
for _ in range(N):
    X, Y = map(int,input().split())
    if X not in Dic_X:
        Dic_X[X] = SortedSet([Y])
    else:
        Dic_X[X].add(Y)
    if Y not in Dic_Y:
        Dic_Y[Y] = SortedSet([X])
    else:
        Dic_Y[Y].add(X)

# print(Dic_X)
# print(Dic_Y)

for _ in range(M):
    D, C = map(str,input().split())
    C = int(C)
    if D == "L":
        L = S_X - C
        R = S_X
        if S_Y in Dic_Y:
            check = True
            while check:
                x = Dic_Y[S_Y].ge(L)
                if x is None:
                    check = False
                elif x > R:
                    check = False
                else:
                    Dic_Y[S_Y].discard(x)
                    Dic_X[x].discard(S_Y)
        S_X -= C
    elif D == "R":
        L = S_X
        R = S_X + C
        if S_Y in Dic_Y:
            check = True
            while check:
                x = Dic_Y[S_Y].ge(L)
                if x is None:
                    check = False
                elif x > R:
                    check = False
                else:
                    Dic_Y[S_Y].discard(x)
                    Dic_X[x].discard(S_Y)
        S_X += C
    elif D == "D":
        L = S_Y - C
        R = S_Y
        if S_X in Dic_X:
            check = True
            while check:
                y = Dic_X[S_X].ge(L)
                if y is None:
                    check = False
                elif y > R:
                    check = False
                else:
                    Dic_X[S_X].discard(y)
                    Dic_Y[y].discard(S_X)
        S_Y -= C
    else:
        L = S_Y
        R = S_Y + C
        if S_X in Dic_X:
            check = True
            while check:
                y = Dic_X[S_X].ge(L)
                if y is None:
                    check = False
                elif y > R:
                    check = False
                else:
                    Dic_X[S_X].discard(y)
                    Dic_Y[y].discard(S_X)
        S_Y += C

# print(S_X, S_Y)
# print(Dic_X)
# print(Dic_Y)

ans = N
for x in Dic_X.keys():
    ans -= len(Dic_X[x])

print(S_X, S_Y, ans)