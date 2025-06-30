H, W, X, Y = map(int,input().split())

X -= 1
Y -= 1

S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

T = str(input())

Visited = [[False for _ in range(W)] for _ in range(H)]

for k in range(len(T)):
    if T[k] == "U":
        if X-1 >= 0:
            if S[X-1][Y] != "#":
                X -= 1
    elif T[k] == "D":
        if X+1 < H:
            if S[X+1][Y] != "#":
                X += 1
    elif T[k] == "L":
        if Y-1 >= 0:
            if S[X][Y-1] != "#":
                Y -= 1
    else:
        if Y+1 < W:
            if S[X][Y+1] != "#":
                Y += 1
    
    if S[X][Y] == "@":
        Visited[X][Y] = True
X += 1
Y += 1

ans = 0
for i in range(H):
    for j in range(W):
        if Visited[i][j]:
            ans += 1

print(X, Y, ans)