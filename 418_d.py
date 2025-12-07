N = int(input())
T = str(input())

DP = [[0, 0, 0, 0] for _ in range(N)]
if T[0] == "1":
    DP[0][3] = 1
else:
    DP[0][2] = 1

for i in range(1, N):
    if T[i] == "0":
        DP[i][0] = DP[i-1][2]
        DP[i][1] = DP[i-1][3]
        DP[i][2] = DP[i-1][0] + 1
        DP[i][3] = DP[i-1][1]
    else:
        DP[i][0] = DP[i-1][3]
        DP[i][1] = DP[i-1][2]
        DP[i][2] = DP[i-1][1]
        DP[i][3] = DP[i-1][0] + 1

ans = 0
for i in range(N):
    # print(DP[i])
    ans += DP[i][0] + DP[i][3]

print(ans)