import math
import itertools

N, M = map(int,input().split())

d = M - 10*(N-1) - 1
num = 0
for i in range(d+1):
    num += math.comb(N+i-1, i)
print(num)

Ls = [[0 for _ in range(N)] for _ in range(num)]
ind = 0
for i in range(d+1):
    for v in itertools.combinations_with_replacement(range(N), i):
        for x in v:
            Ls[ind][x] += 1
        ind += 1

Ls.sort()
for l in Ls:
    ans = [1 for _ in range(N)]
    ans[0] += l[0]
    for i in range(1, N):
        ans[i] = ans[i-1] + 10 + l[i]
    print(*ans)