S_pri = str(input())
S = S_pri[::-1]
# print(S)
N = len(S)

p = 10 ** 9 + 7
DP = [
        [
            [0 for _ in range(13)] 
        for _ in range(10)]
    for _ in range(N)]

def dpchange(i, j):
    for k in range(10):
        for x in range(13):
            u = (x + (t*j)) % 13
            DP[i][j][u] += DP[i-1][k][x]
    for y in range(12):
        DP[i][j][y] %= p

if S[0] == "?":
    for j in range(10):
        DP[0][j][j] = 1
else:
    j = int(S[0])
    DP[0][j][j] = 1

for i in range(1, N):
    t = pow(10, i, 13)
    if S[i] == "?":
        for j in range(10):
            dpchange(i, j)
    else:
        j = int(S[i])
        dpchange(i, j)

# for i in range(N):
#     print("digit is", i)
#     for j in range(10):
#         print(j, DP[i][j])

ans = 0
for j in range(10):
    ans += DP[N-1][j][5]

print(ans % p)