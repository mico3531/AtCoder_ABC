def solve(H, W):
    if H <= W:
        S = [[] for _ in range(H)]
        for i in range(H):
            S[i] = list(str(input()))
    else:
        pre_S = ["" for _ in range(H)]
        for i in range(H):
            pre_S[i] = list(str(input()))
        S = [list(x) for x in zip(*pre_S)]
        H, W = W, H

    F = [[-(i*j) / 2 for j in range(W)] for i in range(H)]

    for i in range(H):
        for j in range(W):
            if j != 0:
                F[i][j] += F[i][j-1]
            if S[i][j] == "#":
                F[i][j] += 1
    
    for j in range(W):
        for i in range(1, H):
            F[i][j] += F[i-1][j]
    
    for i in range(H):
        print(F[i])



T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    solve(H, W)