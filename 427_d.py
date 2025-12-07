def solve():
    N, M, K = map(int, input().split())
    S = str(input())

    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)

    DP = [[0 for _ in range(N)] for _ in range(2*K+1)]

    for j in range(N):
        if S[j] == "A":
            DP[0][j] = 1
        else:
            DP[0][j] = 0
    
    count = 1
    for i in range(K):
        for j in range(N):
            DP[count][j] = 1
            for v in G[j]:
                if DP[count-1][v] == 0:
                    DP[count][j] = 0
        count += 1

        for j in range(N):
            DP[count][j] = 0
            for v in G[j]:
                if DP[count-1][v] == 1:
                    DP[count][j] = 1
        count += 1

    if DP[-1][0] == 1:
        print("Alice")
    else:
        print("Bob")

T = int(input())
for _ in range(T):
    solve()