import heapq

def solve(G, N, M, X, Y):
    dist = [10000 for _ in range(N)]
    Queue = []
    heapq.heapify(Queue)
    heapq.heappush(Queue, [0, Y])
    while len(Queue) > 0:
        data = heapq.heappop(Queue)
        d = data[0]
        now = data[1]
        if d < dist[now]:
            dist[now] = d
            for next in G[now]:
                if dist[next] == 10000:
                    heapq.heappush(Queue, [d+1, next])
    print(dist)
    return 0

T = int(input())

for _ in range(T):
    N, M, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    X -= 1
    Y -= 1
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    solve(G, N, M, X, Y)