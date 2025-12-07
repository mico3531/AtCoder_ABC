H, W = map(int, input().split())

S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = "Yes"

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            count = 0
            for t in range(4):
                ni = i + dx[t]
                nj = j + dy[t]
                if 0 <= ni and ni < H and 0 <= nj and nj < W:
                    if S[ni][nj] == "#":
                        count += 1
            if count not in [2, 4]:
                ans = "No"

print(ans)