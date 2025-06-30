H, W, K = map(int,input().split())

S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

visited = [[False for _ in range(W)] for _ in range(H)]
ans = 0
def dfs(i, j, k):
    global ans
    if k == K:
        ans += 1
        return
    visited[i][j] = True
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        i2 = i+x
        j2 = j+y
        if 0 <= i2 < H and 0 <= j2 < W:
            if S[i2][j2] == "." and not visited[i2][j2]:
                dfs(i2, j2, k+1)
    visited[i][j] = False

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            dfs(i,j,0)

print(ans)