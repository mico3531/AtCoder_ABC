N = int(input())
X, Y = map(int,input().split())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for i in range(N):
    A[i], B[i] = map(int,input().split())

DP = [[[1000 for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
DP[0][0][0] = 0

for i in range(N):
    for j in range(X+1):
        for k in range(Y+1):
            DP[i+1][j][k] = DP[i][j][k]
            pre_j = max(0, j-A[i])
            pre_k = max(0, k-B[i])
            DP[i+1][j][k] = min(DP[i+1][j][k], DP[i][pre_j][pre_k] + 1)

# for i in range(N+1):
#     print(DP[i])

ans = DP[-1][X][Y]
if ans == 1000:
    print(-1)
else:
    print(ans)