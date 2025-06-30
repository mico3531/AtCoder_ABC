H, W = map(int, input().split())
S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

L = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    count = 0
    for j in range(W):
        if S[i][j] == "#":
            count = 0
        else:
            count += 1
        L[i][j] = count

R = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    count = 0
    for j in range(W-1, -1, -1):
        if S[i][j] == "#":
            count = 0
        else:
            count += 1
        R[i][j] = count

U = [[0 for _ in range(W)] for _ in range(H)]
for j in range(W):
    count = 0
    for i in range(H):
        if S[i][j] == "#":
            count = 0
        else:
            count += 1
        U[i][j] = count

D = [[0 for _ in range(W)] for _ in range(H)]
for j in range(W):
    count = 0
    for i in range(H-1, -1, -1):
        if D[i][j] == "#":
            count = 0
        else:
            count += 1
        D[i][j] = count

ans = 0
for i in range(H):
    for j in range(W):
        count = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
        ans = max(ans, count)

print(ans)