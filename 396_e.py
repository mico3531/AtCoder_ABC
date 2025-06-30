from collections import deque

N, M = map(int,input().split())

G = [[] for _ in range(N)]

for i in range(M):
    x, y, z = list(map(int,input().split()))
    x -= 1
    y -= 1
    G[x].append([y, z])
    G[y].append([x, z])

Visited = [False for _ in range(N)]
Value = [-1 for _ in range(N)]

def bfs(start):
    Queue = deque([start])
    Visited[start] = True
    Conn_comp = set([start])
    
    while len(Queue) > 0:
        x = Queue.popleft()
        for Next in G[x]:
            y = Next[0]
            z = Next[1]
            
            if not Visited[y]:
                Visited[y] = True
                Value[y] = Value[x] ^ z
                Queue.append(y)
                Conn_comp.add(y)
            
            else:
                if Value[y] != Value[x] ^ z:
                    print(-1)
                    exit()
    
    return Conn_comp

Ans = [0 for _ in range(N)]

for start in range(N):
    if Visited[start]:
        continue
    
    Value[start] = 0
    Conn_comp = bfs(start)
    
    for t in range(30):
        count = 0
        for x in Conn_comp:
            if (Value[x] >> t) & 1:
                count += 1
        
        if count < len(Conn_comp) - count:
            for x in Conn_comp:
                if (Value[x] >> t) & 1:
                    Ans[x] += 2 ** t
        
        else:
            for x in Conn_comp:
                if not (Value[x] >> t) & 1:
                    Ans[x] += 2 ** t

print(*Ans)