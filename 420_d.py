from collections import deque

H, W = map(int, input().split())

A = ["" for _ in range(H)]
for i in range(H):
    A[i] = str(input())

B = ["" for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == "o":
            B[i] += "x"
        elif A[i][j] == "x":
            B[i] += "o"
        else:
            B[i] += A[i][j]

Dist_A = [[10 ** 10 for _ in range(W)] for _ in range(H)]
Dist_B = [[10 ** 10 for _ in range(W)] for _ in range(H)]

Queue = deque([])
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            Queue.append(["A", i, j])
            Dist_A[i][j] = 0
        if A[i][j] == "G":
            gx = i
            gy = j

direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while len(Queue) > 0:
    now = Queue.popleft()
    x = now[1]
    y = now[2]

    if now[0] == "A":
        for t in range(4):
            z = x + direct[t][0]
            w = y + direct[t][1]
            if 0 <= z and z < H and 0 <= w and w < W:
                if A[z][w] in [".", "S", "G", "o"]:
                    if Dist_A[z][w] == 10 ** 10:
                        Dist_A[z][w] = Dist_A[x][y] + 1
                        Queue.append(["A", z, w])
                elif A[z][w] == "?":
                    if Dist_B[z][w] == 10 ** 10:
                        Dist_B[z][w] = Dist_A[x][y] + 1
                        Queue.append(["B", z, w])
    
    else:
        for t in range(4):
            z = x + direct[t][0]
            w = y + direct[t][1]
            if 0 <= z and z < H and 0 <= w and w < W:
                if B[z][w] in [".", "S", "G", "o"]:
                    if Dist_B[z][w] == 10 ** 10:
                        Dist_B[z][w] = Dist_B[x][y] + 1
                        Queue.append(["B", z, w])
                elif B[z][w] == "?":
                    if Dist_A[z][w] == 10 ** 10:
                        Dist_A[z][w] = Dist_B[x][y] + 1
                        Queue.append(["A", z, w])

ans = min(Dist_A[gx][gy], Dist_B[gx][gy])

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)