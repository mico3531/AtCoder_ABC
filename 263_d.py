N, L, R = map(int,input().split())
A = list(map(int,input().split()))

F = [0 for _ in range(N+1)]
for i in range(1, N+1):
    F[i] = min(F[i-1] + A[i-1], i * L)

G = [0 for _ in range(N+1)]
for i in range(1, N+1):
    G[i] = min(G[i-1] + A[N-i] , i * R)

# print(F)
# print(G)
ans = F[0] + G[N]
for i in range(N+1):
    ans = min(ans, F[i] + G[N-i])
print(ans)

# AC