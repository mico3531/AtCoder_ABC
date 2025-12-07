from collections import deque
import copy

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

S = str(input())

D_1 = [[-1, 0] for _ in range(N)]
D_2 = [[-2, 10**10] for _ in range(N)]
Queue = deque([])

for i in range(N):
    if S[i] == "S":
        Queue.append(i)
        D_1[i][0] = i
    else:
        D_1[i][1] = 10 ** 10

while len(Queue) > 0:
    x = Queue.popleft()
    check = False

    for y in G[x]:
        if D_1[y][1] > D_1[x][1] + 1:
            if D_1[y][0] != D_1[x][0]:
                D_2[y] = copy.copy(D_1[y])
                D_1[y][1] = D_1[x][1] + 1
                D_1[y][0] = D_1[x][0]
            else:
                D_1[y][1] = D_1[x][1] + 1
            check = True
        
        if D_2[y][1] > D_1[x][1] + 1:
            if D_1[y][0] != D_1[x][0]:
                D_2[y][0] = D_1[x][0]
                D_2[y][1] = D_1[x][1] + 1
                check = True
        
        if D_1[y][1] > D_2[x][1] + 1:
            if D_1[y][0] != D_2[x][0]:
                D_2[y] = copy.copy(D_1[y])
                D_1[y][0] = D_2[x][0]
                D_1[y][1] = D_2[x][1] + 1
            else:
                D_1[y][1] = D_2[x][1] + 1
            check = True
        
        if D_2[y][1] > D_2[x][1] + 1:
            if D_1[y][0] != D_2[x][0]:
                D_2[y][0] = D_2[x][0]
                D_2[y][1] = D_2[x][1] + 1
                check = True
    
        if check:
            Queue.append(y)

# print(D_1)
# print(D_2)

for i in range(N):
    if S[i] == "D":
        print(D_1[i][1] + D_2[i][1])