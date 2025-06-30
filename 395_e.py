import heapq

N, M, X = map(int,input().split())

G = [set() for _ in range(2*N+1)]

for u in range(1, N+1):
    G[u].add((X, u+N))
    G[u+N].add((X, u))

for _ in range(M):
    u, v = map(int,input().split())
    G[u].add((1, v))
    G[v+N].add((1, u+N))

Dist = [float("INF") for _ in range(2*N+1)]
Dist[1] = 0
Queue = [(0, 1)]
heapq.heapify(Queue)

while len(Queue) > 0:
    Now = heapq.heappop(Queue)
    d = Now[0]
    x = Now[1]

    if d <= Dist[x]:
        for Next in G[x]:
            cost = Next[0]
            y = Next[1]
            if d + cost < Dist[y]:
                Dist[y] = d + cost
                heapq.heappush(Queue, (d+cost, y))

# print(Dist)
print(min(Dist[N], Dist[2*N]))