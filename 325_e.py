import heapq

N, A, B, C = map(int, input().split())

D = [[] for _ in range(2* N)]
for i in range(N):
    D_i = list(map(int, input().split()))
    for j in range(N):
        D[i].append([A * D_i[j], j])
        D[i+N].append([B * D_i[j] + C, j + N])
    D[i].append([0, i+N])

Dist = [float("INF") for _ in range(2*N)]
Dist[0] = 0
Queue = [[0,0]]
heapq.heapify(Queue)

while len(Queue) > 0:
    Now = heapq.heappop(Queue)
    now_dist, x = Now[0], Now[1]
    if now_dist == Dist[x]:
        for Next in D[x]:
            next_dist = now_dist + Next[0]
            y = Next[1]
            if next_dist < Dist[y]:
                Dist[y] = next_dist
                heapq.heappush(Queue, [next_dist, y])

print(Dist[-1])