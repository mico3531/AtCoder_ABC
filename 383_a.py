N = int(input())

T = [0 for _ in range(N)]
V = [0 for _ in range(N)]
for i in range(N):
    T[i], V[i] = map(int,input().split())

ans = 0
for tt in range(T[-1]+1):
    if ans >= 1:
        ans -= 1
    if tt in T:
        i = T.index(tt)
        ans += V[i]
    # print(ans)

print(ans)