from collections import deque

H, W, D = map(int,input().split())
S = ["" for _ in range(H)]

for i in range(H):
    S[i] = str(input())

dist = [[10 ** 6 for _ in range(W)] for _ in range(H)]
d = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            dist[i][j] = 0
            d.append([i, j])

while len(d) > 0:
    v = d.popleft()
    i = v[0]
    j = v[1]
    if 1 <= i:
        if S[i-1][j] == "." and dist[i-1][j] == 10 ** 6:
            dist[i-1][j] = dist[i][j] + 1
            d.append([i-1, j])
    if i < H-1:
        if S[i+1][j] == "." and dist[i+1][j] == 10 ** 6:
            dist[i+1][j] = dist[i][j] + 1
            d.append([i+1, j])
    if 1 <= j:
        if S[i][j-1] == "." and dist[i][j-1] == 10 ** 6:
            dist[i][j-1] = dist[i][j] + 1
            d.append([i, j-1])
    if j < W-1:
        if S[i][j+1] == "." and dist[i][j+1] == 10 ** 6:
            dist[i][j+1] = dist[i][j] + 1
            d.append([i, j+1])

ans = 0
for i in range(H):
    for j in range(W):
        if dist[i][j] <= D:
            ans += 1
print(ans)