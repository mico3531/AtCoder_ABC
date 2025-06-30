N, H, M = map(int, input().split())

DP = [M for _ in range(H+1)]

ans = 0
for i in range(N):
    a, b = map(int, input().split())
    for j in range(H+1):
        DP[j] -= b
        if j+a <= H:
            DP[j] = max(DP[j], DP[j+a])
    if DP[0] >= 0:
        ans += 1

print(ans)