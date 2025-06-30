N, K = map(int,input().split())
P = list(map(int,input().split()))

E = [0 for _ in range(N)]

for i in range(N):
    E[i] = (P[i] + 1) / 2

S = 0
for i in range(K):
    S += E[i]

ans = S
for i in range(N-K):
    S -= E[i]
    S += E[i+K]
    ans = max(S, ans)

print(ans)