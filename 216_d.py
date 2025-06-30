from collections import deque

N, M = map(int, input().split())

Count = [[] for _ in range(N+1)]
A = [[] for _ in range(M)]
Queue = deque([])

for i in range(M):
    k = int(input())
    A[i] = deque(list(map(int, input().split())))
    x = A[i].popleft()
    Count[x].append(i)
    if len(Count[x]) == 2:
        Queue.append(x)

while len(Queue) > 0:
    x = Queue.popleft()
    for i in Count[x]:
        if len(A[i]) > 0:
            y = A[i].popleft()
            Count[y].append(i)
            if len(Count[y]) == 2:
                Queue.append(y)

for i in range(M):
    if len(A[i]) > 0:
        print("No")
        exit()
print("Yes")