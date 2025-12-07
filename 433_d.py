import math
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [[0]]
for d in range(1, 11):
    Ls = []
    for i in range(N):
        t = -A[i] * 10**d
        t %= M
        Ls.append(t)
    Ls.sort()
    B.append(Ls)

ans = 0
for j in range(N):
    k = math.floor(math.log10(A[j])) + 1
    l = bisect.bisect_left(B[k], A[j] % M)
    r = bisect.bisect_right(B[k], A[j] % M)
    ans += r-l
print(ans)