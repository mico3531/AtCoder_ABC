from collections import deque

H, W = map(int,input().split())
A = ["" for _ in range(H)]
for i in range(H):
    A[i] = str(input())

G = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    visible = False
    for j in range(W):
        if visible:
            G[i][j] = 1
            if A[i][j] not in [">", "."]:
                visible = False
        else:
            if A[i][j] == ">":
                G[i][j] = 1
                visible = True
            elif A[i][j] not in [".", "S", "G"]:
                G[i][j] = 1
    
    visible = False
    for j in range(W-1, -1, -1):
        if visible:
            G[i][j] = 1
            if A[i][j] not in ["<", "."]:
                visible = False
        else:
            if A[i][j] == "<":
                G[i][j] = 1
                visible = True
            elif A[i][j] not in [".", "S", "G"]:
                G[i][j] = 1

for j in range(W):
    visible = False
    for i in range(H):
        if visible:
            G[i][j] = 1
            if A[i][j] not in ["v", "."]:
                visible = False
        else:
            if A[i][j] == "v":
                G[i][j] = 1
                visible = True
            elif A[i][j] not in [".", "S", "G"]:
                G[i][j] = 1
    
    visible = False
    for i in range(H-1, -1, -1):
        if visible:
            G[i][j] = 1
            if A[i][j] not in ["^", "."]:
                visible = False
        else:
            if A[i][j] == "^":
                G[i][j] = 1
                visible = True
            elif A[i][j] not in [".", "S", "G"]:
                G[i][j] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start_i = i
            start_j = j
        elif A[i][j] == "G":
            goal_i = i
            goal_j = j

Dist = [[10**7 for _ in range(W)] for _ in range(H)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Queue = deque([])
Queue.append([start_i, start_j])

Dist[start_i][start_j] = 0

while len(Queue) > 0:
    now = Queue.popleft()
    now_i = now[0]
    now_j = now[1]
    for t in range(4):
        next_i = now_i + dx[t]
        next_j = now_j + dy[t]
        if 0 <= next_i and next_i < H and 0 <= next_j and next_j < W:
            if G[next_i][next_j] == 0 and Dist[next_i][next_j] == 10**7:
                Queue.append([next_i, next_j])
                Dist[next_i][next_j] = Dist[now_i][now_j] + 1

# for i in range(H):
#     print(Dist[i])

if Dist[goal_i][goal_j] == 10**7:
    print(-1)
else:
    print(Dist[goal_i][goal_j])
