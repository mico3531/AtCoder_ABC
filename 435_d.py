from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
G_rev = [[] for _ in range(N+1)]
check = [False for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    G[X].append(Y)
    G_rev[Y].append(X)

Q = int(input())

for _ in range(Q):
    q_type, v = map(int, input().split())
    if q_type == 1:
        if not check[v]:
            Queue = deque([v])
            while len(Queue) > 0:
                x = Queue.popleft()
                check[x] = True
                for y in G_rev[x]:
                    if not check[y]:
                        Queue.append(y)
    else:
        if check[v]:
            print("Yes")
        else:
            print("No")