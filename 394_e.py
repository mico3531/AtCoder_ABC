from collections import deque

N = int(input())

C = ["" for _ in range(N)]
for i in range(N):
    C[i] = str(input())

Dist = [-1 for _ in range(N**2 + 1)]
Dist[-1] = 0
Queue = deque([])

for i in range(N):
    Dist[N*i + i] = 0
    Queue.append(N*i + i)

for i in range(N):
    for j in range(N):
        if C[i][j] != "-" and i != j:
            Dist[N*i + j] = 1
            Queue.append(N*i + j)

while len(Queue) > 0:
    s = Queue.popleft()
    for t in range(N ** 2):
        i = s // N
        j = s % N
        k = t // N
        l = t % N
        if Dist[t] == -1:
            if C[k][i] != "-" and C[k][i] == C[j][l]:
                Dist[t] = Dist[s] + 2
                Queue.append(t)


for i in range(N):
    Ls = [Dist[N*i + j] for j in range(N)]
    print(*Ls)