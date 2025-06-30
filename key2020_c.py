N, K, S = map(int,input().split())

if S == 10 ** 9:
    ans = [1 for _ in range(N)]
    for i in range(K):
        ans[i] = 10 ** 9
else:
    ans = [S+1 for _ in range(N)]
    for i in range(K):
        ans[i] = S

print(*ans)