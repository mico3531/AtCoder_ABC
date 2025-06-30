from collections import deque

H, W = map(int,input().split())
S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

pos_S = [0,0]
pos_G = [0,0]
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            pos_S = [i, j]
        elif S[i][j] == "G":
            pos_G = [i, j]

def check(i, j):
    if 0 <= i and i < H and 0 <= j and j < W:
        return True
    else:
        return False

V_1 = [[1, 0], [-1, 0]]
V_2 = [[0, 1], [0, -1]]

D_1 = [[-1 for _ in range(W)] for _ in range(H)]
D_1[pos_S[0]][pos_S[1]] = 0

Queue_1 = deque()
Queue_1.append(pos_S)
while len(Queue_1) > 0:
    now = Queue_1.popleft()
    par = (now[0] + now[1]) % 2
    if par == 0:
        for v in V_1:
            Next = [now[0] + v[0], now[1] + v[1]]
            if check(Next[0], Next[1]):
                if S[Next[0]][Next[1]] != "#":
                    if D_1[Next[0]][Next[1]] == -1:
                        D_1[Next[0]][Next[1]] = D_1[now[0]][now[1]] + 1
                        Queue_1.append(Next)
    else:
        for v in V_2:
            Next = [now[0] + v[0], now[1] + v[1]]
            if check(Next[0], Next[1]):
                if S[Next[0]][Next[1]] != "#":
                    if D_1[Next[0]][Next[1]] == -1:
                        D_1[Next[0]][Next[1]] = D_1[now[0]][now[1]] + 1
                        Queue_1.append(Next)

D_2 = [[-1 for _ in range(W)] for _ in range(H)]
D_2[pos_S[0]][pos_S[1]] = 0

Queue_2 = deque()
Queue_2.append(pos_S)
while len(Queue_2) > 0:
    now = Queue_2.popleft()
    par = (now[0] + now[1]) % 2
    if par == 1:
        for v in V_1:
            Next = [now[0] + v[0], now[1] + v[1]]
            if check(Next[0], Next[1]):
                if S[Next[0]][Next[1]] != "#":
                    if D_2[Next[0]][Next[1]] == -1:
                        D_2[Next[0]][Next[1]] = D_2[now[0]][now[1]] + 1
                        Queue_2.append(Next)
    else:
        for v in V_2:
            Next = [now[0] + v[0], now[1] + v[1]]
            if check(Next[0], Next[1]):
                if S[Next[0]][Next[1]] != "#":
                    if D_2[Next[0]][Next[1]] == -1:
                        D_2[Next[0]][Next[1]] = D_2[now[0]][now[1]] + 1
                        Queue_2.append(Next)

dis_1 = D_1[pos_G[0]][pos_G[1]]
dis_2 = D_2[pos_G[0]][pos_G[1]]
if dis_1 != -1:
    if dis_2 != -1:
        print(min(dis_1, dis_2))
    else:
        print(dis_1)
else:
    if dis_2 != -1:
        print(dis_2)
    else:
        print(-1)