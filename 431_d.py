N = int(input())

W = [0 for _ in range(N)]
H = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    W[i] = line[0]
    H[i] = line[1]
    B[i] = line[2]

lim_W = sum(W) // 2

DP = [0 for _ in range(lim_W + 1)]
for i in range(N):
    for t in range(lim_W, -1, -1):
        if t >= W[i]:
            DP[t] = max(DP[t] + B[i], DP[t-W[i]] + H[i])
        else:
            DP[t] += B[i]

print(max(DP))