S = ["" for _ in range(8)]

for i in range(8):
    S[i] = str(input())

avoid = [[1 for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            for k in range(8):
                avoid[i][k] = 0
                avoid[k][j] = 0

ans = 0
for i in range(8):
    for j in range(8):
        ans += avoid[i][j]

print(ans)