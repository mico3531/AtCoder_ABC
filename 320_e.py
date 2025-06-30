import heapq

N, M = map(int, input().split())
Member = list(range(N))
heapq.heapify(Member)

Query = []
heapq.heapify(Query)

for _ in range(M):
    T, W, S = map(int, input().split())
    heapq.heappush(Query, [T, 1, W, T+S])

Ans = [0 for _ in range(N)]
while len(Query) > 0:
    now = heapq.heappop(Query)
    if now[1] == 1:
        if len(Member) > 0:
            x = heapq.heappop(Member)
            Ans[x] += now[2]
            heapq.heappush(Query, [now[3], 0, x])
    else:
        x = now[2]
        heapq.heappush(Member, x)

for i in range(N):
    print(Ans[i])