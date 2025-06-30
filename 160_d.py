from collections import deque

N, X, Y = map(int,input().split())
X -= 1
Y -= 1

G = [[] for _ in range(N)]
for i in range(N):
    if i > 0:
        G[i].append(i-1)
    if i < N-1:
        G[i].append(i+1)
    if i == X:
        G[i].append(Y)
    if i == Y:
        G[i].append(X)

Ans = [0 for _ in range(N)]
for s in range(N):
    D = [10 ** 5 for _ in range(N)]
    D[s] = 0

    Visited = [False for _ in range(N)]
    Visited[s] = True
    
    Queue = deque([s])
    while len(Queue) > 0:
        x = Queue.popleft()
        for y in G[x]:
            if not Visited[y]:
                Visited[y] = True
                Queue.append(y)
                D[y] = min(D[x]+1, D[y])
    
    for i in range(N):
        Ans[D[i]] += 1

for i in range(1, N):
    print(Ans[i] // 2)