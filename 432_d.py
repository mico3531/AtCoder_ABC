import copy
from collections import deque

N, X, Y = map(int, input().split())

Ls_sq = [[0, 0, X, Y]]

for _ in range(N):
    Query = list(map(str, input().split()))
    C = str(Query[0])
    A = int(Query[1])
    B = int(Query[2])

    Ls_new = []

    for sq in Ls_sq:
        dx = sq[0]
        dy = sq[1]
        ux = sq[2]
        uy = sq[3]
        if C == "X":
            if ux <= A:
                Ls_new.append([dx, dy - B, ux, uy - B])
            elif dx < A:
                Ls_new.append([dx, dy - B, A, uy - B])
                Ls_new.append([A, dy + B, ux, uy + B])
            else:
                Ls_new.append([dx, dy + B, ux, uy + B])
        else:
            if uy <= A:
                Ls_new.append([dx - B, dy, ux - B, uy])
            elif dy < A:
                Ls_new.append([dx - B, dy, ux - B, A])
                Ls_new.append([dx + B, A, ux + B, uy])
            else:
                Ls_new.append([dx + B, dy, ux + B, uy])

    Ls_sq = copy.copy(Ls_new)

    # print(Ls_sq)

Area = [0 for _ in range(len(Ls_sq))]
G = [set() for _ in range(len(Ls_sq))]
for i in range(len(Ls_sq)):
    sq = Ls_sq[i]
    dx = sq[0]
    dy = sq[1]
    ux = sq[2]
    uy = sq[3]
    
    Area[i] = (ux - dx) * (uy - dy)

    for j in range(len(Ls_sq)):
        sq2 = Ls_sq[j]
        dx2 = sq2[0]
        dy2 = sq2[1]
        ux2 = sq2[2]
        uy2 = sq2[3]

        conn = False

        if dx == ux2 or ux == dx2:
            if max(dy , dy2) < min(uy, uy2):
                conn = True
        elif dy == uy2 or uy == dy2:
            if max(dx, dx2) < min(ux, ux2):
                conn = True
        
        if conn:
            G[i].add(j)

# print(Area)
# print(G)

Ans = []
check = [False for _ in range(len(G))]

for i in range(len(G)):
    if not check[i]:
        total = Area[i]
        Queue = deque([i])
        check[i] = True
        while len(Queue) > 0:
            x = Queue.popleft()
            for y in G[x]:
                if not check[y]:
                    Queue.append(y)
                    total += Area[y]
                    check[y] = True
        Ans.append(total)

Ans.sort()
print(len(Ans))
print(*Ans)