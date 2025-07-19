N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

Ls_d = [X[i+1] - X[i] for i in range(N-1)]
Ls_d.sort()

ans = 0
for i in range(N-M):
    ans += Ls_d[i]

print(ans)