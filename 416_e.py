N, M = map(int, input().split())

Dist = [[10 ** 12 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    Dist[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    if C < Dist[A][B]:
        Dist[A][B] = C
    if C < Dist[B][A]:
        Dist[B][A] = C

K, T = map(int, input().split())
D = list(map(int, input().split()))
for i in range(K):
    Dist[D[i]][0] = T
    Dist[0][D[i]] = 0

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if Dist[i][k] + Dist[k][j] < Dist[i][j]:
                Dist[i][j] = Dist[i][k] + Dist[k][j]

Q = int(input())
for _ in range(Q):
    Query = list(map(int, input().split()))
    
    if Query[0] == 1:
        x = Query[1]
        y = Query[2]
        t = Query[3]
        for i in range(N+1):
            for j in range(N+1):
                cost_1 = Dist[i][x] + t + Dist[y][j]
                cost_2 = Dist[i][y] + t + Dist[x][j]
                if cost_1 < Dist[i][j]:
                    Dist[i][j] = cost_1
                if cost_2 < Dist[i][j]:
                    Dist[i][j] = cost_2
    
    elif Query[0] == 2:
        x = Query[1]
        for i in range(N+1):
            for j in range(N+1):
                cost_1 = Dist[i][x] + T + Dist[0][j]
                cost_2 = Dist[i][0] + Dist[x][j]
                if cost_1 < Dist[i][j]:
                    Dist[i][j] = cost_1
                if cost_2 < Dist[i][j]:
                    Dist[i][j] = cost_2
    
    else:
        ans = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if Dist[i][j] != 10 ** 12:
                    ans += Dist[i][j]
        print(ans)