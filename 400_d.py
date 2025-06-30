from collections import deque

H, W = map(int,input().split())

City = ["" for _ in range(H)]
for i in range(H):
    City[i] = str(input())

A, B, C, D = map(int,input().split())
A -= 1
B -= 1
C -= 1
D -= 1

Dist = [[2*H*W for _ in range(W)] for _ in range(H)]
Dist[A][B] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Queue = deque([A*W + B])

while len(Queue) > 0:
    num = Queue.popleft()
    x = num // W
    y = num % W
    if x == C and y == D:
        break

    for t in range(4):
        for u in range(1,3):
            nx = x + u * dx[t]
            ny = y + u * dy[t]
            if 0 <= nx and nx < H and 0 <= ny and ny < W:
                if City[nx][ny] == "." and u == 1:
                    if Dist[nx][ny] > Dist[x][y]:
                        Dist[nx][ny] = Dist[x][y]
                        Queue.appendleft(nx*W + ny)
                else:
                    if Dist[nx][ny] > Dist[x][y] + 1:
                        Dist[nx][ny] = Dist[x][y] + 1
                        Queue.append(nx*W + ny)

print(Dist[C][D])