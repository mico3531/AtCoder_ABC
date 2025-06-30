from collections import deque
import heapq

Q = int(input())

sort_A = []
heapq.heapify(sort_A)
unsort_A = deque([])

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        x = Query[1]
        unsort_A.append(x)
    elif Query[0] == 2:
        if len(sort_A) > 0:
            print(heapq.heappop(sort_A))
        else:
            print(unsort_A.popleft())
    else:
        for x in unsort_A:
            heapq.heappush(sort_A, x)
        unsort_A = deque([])