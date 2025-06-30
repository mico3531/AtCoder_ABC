N, M, K = map(int, input().split())
mod = 998244353

G = [[1 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1][v-1] = 0
    G[v-1][u-1] = 0
for i in range(N):
    G[i][i] = 0

G_list = [G for _ in range(15)]

def mat_multi(A, B, N):
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= mod
    return C

for i in range(1, 15):
    G_list[i] = mat_multi(G_list[i-1], G_list[i-1], N)

# for i in range(15):
#     print(i)
#     print(G_list[i])


Ans = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    Ans[i][i] = 1

for t in range(15):
    if (K >> t) & 1:
        print(t)
        Ans = mat_multi(Ans, G_list[t], N)

ans = 0
for i in range(N):
    print(Ans[i])
    ans += Ans[i][0]
print(ans % mod)