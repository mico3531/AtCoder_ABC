N, X = map(int, input().split())

S = [0 for _ in range(N)]
C = [0 for _ in range(N)]
P = [0 for _ in range(N)]

for i in range(N):
    S[i], C[i], P[i] = map(int, input().split())
    P[i] *= 0.01

DP = [[0.0 for _ in range(X+1)] for _ in range(2 ** N)]

for x in range(X+1):
    for t in range(2**N):
        for i in range(N):
            before_money = x - C[i]
            if (not (t >> i) & 1) and before_money >= 0:
                before_t = t + 2**i
                val = (DP[before_t][before_money] + S[i]) * P[i]
                val += DP[t][before_money] * (1-P[i])
                DP[t][x] = max(DP[t][x], val)

# for t in range(2**N):
#     print(DP[t])
print(DP[0][-1])