N, M = map(int,input().split())
X = list(map(int,input().split()))

X.sort()

ans = 0

if N < M:
    L = [0 for _ in range(M-1)]
    for i in range(M-1):
        L[i] = X[i+1] - X[i]
    L.sort()
    ans = X[-1] - X[0]
    for k in range(1, N):
        ans -= L[-k]

print(ans)