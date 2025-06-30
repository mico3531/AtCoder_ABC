from collections import deque

H, W = map(int, input().split())
S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

D = [[-1 for _ in range(W)] for _ in range(H)]
Queue = deque([])
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            Queue.append([i, j])
            D[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while len(Queue) > 0:
    now = Queue.popleft()
    now_x = now[0]
    now_y = now[1]
    for t in range(4):
        next_x = now_x + dx[t]
        next_y = now_y + dy[t]
        if 0 <= next_x and next_x < H:
            if 0 <= next_y and next_y < W:
                if D[next_x][next_y] == -1 and S[next_x][next_y] == ".":
                    D[next_x][next_y] = D[now_x][now_y] + 1
                    Queue.append([next_x, next_y])

Ans = [["" for _ in range(W)] for _ in range(H)]
dir = ["^", "v", "<", ">"]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            vect = -1
            for t in range(4):
                next_x = i + dx[t]
                next_y = j + dy[t]
                if 0 <= next_x and next_x < H:
                    if 0 <= next_y and next_y < W:
                        if D[next_x][next_y] + 1 == D[i][j]:
                            vect = t
            Ans[i][j] = dir[vect]
        else:
            Ans[i][j] = S[i][j]

for i in range(H):
    print("".join(Ans[i]))