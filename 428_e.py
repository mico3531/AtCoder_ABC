from collections import deque

N = int(input())

G = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

D_1 = [-1 for _ in range(N)]
D_1[0] = 0
Queue_1 = deque([0])
while len(Queue_1) > 0:
    x = Queue_1.pop()
    for y in G[x]:
        if D_1[y] == -1:
            D_1[y] = D_1[x] + 1
            Queue_1.append(y)

max_dist = 0
s = 0
for i in range(N):
    if D_1[i] >= max_dist:
        max_dist = D_1[i]
        s = i

D_2 = [-1 for _ in range(N)]
D_2[s] = 0
Queue_2 = deque([s])
while len(Queue_2) > 0:
    x = Queue_2.pop()
    for y in G[x]:
        if D_2[y] == -1:
            D_2[y] = D_2[x] + 1
            Queue_2.append(y)

max_dist = 0
t = 0
for i in range(N):
    if D_2[i] >= max_dist:
        max_dist = D_2[i]
        t = i

D_3 = [-1 for _ in range(2*N)]
D_3[t] = 0
Queue_3 = deque([t])
while len(Queue_3) > 0:
    x = Queue_3.pop()
    for y in G[x]:
        if D_3[y] == -1:
            D_3[y] = D_3[x] + 1
            Queue_3.append(y)

# print(D_1)
# print(D_2)
# print(D_3)

for i in range(N):
    if D_2[i] < D_3[i]:
        print(1 + (t % N))
    else:
        print(1 + (s % N))