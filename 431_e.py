from collections import deque

def solve():
    H, W = map(int, input().split())
    S = ["" for _ in range(H)]
    for i in range(H):
        S[i] = str(input())
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    D = [ [ [10**10, 10**10, 10**10, 10**10] 
            for _ in range(W)] 
        for _ in range(H)]
    D[0][0][3] = 0

    Queue = deque()
    Queue.append([0, -1, 1, 0])

    while len(Queue) > 0:
        now = Queue.popleft()
        pre_x, pre_y = now[0], now[1]
        dir, cost = now[2], now[3]
        nx = pre_x + dx[dir]
        ny = pre_y + dy[dir]

        if 0 <= nx < H and 0 <= ny < W:
            for ndir in range(4):
                if S[nx][ny] == "A":
                    if dir == ndir:
                        if D[nx][ny][ndir] > cost:
                            D[nx][ny][ndir] = cost
                            Queue.appendleft([nx, ny, ndir, cost])
                    elif dir ^ ndir != 2:
                        if D[nx][ny][ndir] > cost + 1:
                            D[nx][ny][ndir] = cost + 1
                            Queue.append([nx, ny, ndir, cost + 1])
                elif S[nx][ny] == "B":
                    if dir ^ ndir == 1:
                        if D[nx][ny][ndir] > cost:
                            D[nx][ny][ndir] = cost
                            Queue.appendleft([nx, ny, ndir, cost])
                    elif dir ^ ndir != 2:
                        if D[nx][ny][ndir] > cost + 1:
                            D[nx][ny][ndir] = cost + 1
                            Queue.append([nx, ny, ndir, cost + 1])
                else:
                    if dir ^ ndir == 3:
                        if D[nx][ny][ndir] > cost:
                            D[nx][ny][ndir] = cost
                            Queue.appendleft([nx, ny, ndir, cost])
                    elif dir ^ ndir != 2:
                        if D[nx][ny][ndir] > cost + 1:
                            D[nx][ny][ndir] = cost + 1
                            Queue.append([nx, ny, ndir, cost + 1])
    
    print(D[-1][-1][1])

T = int(input())
for _ in range(T):
    solve()