from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)

def bfs():
    dist = [-1] * N
    dist[0] = 0
    q = deque([0])

    while len(q) > 0:
        x = q.popleft()
        for y in G[x]:
            if y == 0 and dist[x] > 0:
                return dist[x] + 1
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    return -1

ans = bfs()
print(ans)
