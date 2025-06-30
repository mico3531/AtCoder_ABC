from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append([b, w])

Able = [[False for _ in range(1024)] for _ in range(N)]
Able[0][0] = True

Queue = deque([])
Queue.append([0, 0])

while len(Queue) > 0:
    Now = Queue.popleft()
    x = Now[0]
    num = Now[1]
    for Next in G[x]:
        y = Next[0]
        w = Next[1]
        if not Able[y][num^w]:
            Able[y][num^w] = True
            Queue.append([y, num^w])

for num in range(1024):
    if Able[-1][num]:
        print(num)
        exit()
print(-1)