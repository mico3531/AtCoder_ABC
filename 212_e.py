import copy

mod = 998244353

N, M, K = map(int, input().split())

S = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    S[u-1].add(v-1)
    S[v-1].add(u-1)
for i in range(N):
    S[i].add(i)

DP = [0 for _ in range(N)]
DP[0] = 1

for _ in range(K):
    base_count = sum(DP)
    new_DP = [base_count for _ in range(N)]
    for i in range(N):
        for j in S[i]:
            new_DP[i] -= DP[j]
        new_DP[i] %= mod
    DP = copy.copy(new_DP)

print(DP[0])