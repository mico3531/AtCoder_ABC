H, W, K = map(int,input().split())

S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

ans = 10 ** 6

if K <= H:
    for j in range(W):
        D = {"o": 0, "x": 0, ".": 0}
        for i in range(K):
            s = S[i][j]
            D[s] += 1
        if D["x"] == 0:
            ans = min(ans, D["."])
        if K < H:
            for i in range(K, H):
                s1 = S[i-K][j]
                s2 = S[i][j]
                D[s1] -= 1
                D[s2] += 1
                if D["x"] == 0:
                    ans = min(ans, D["."])

if K <= W:
    for i in range(H):
        D = {"o": 0, "x": 0, ".": 0}
        for j in range(K):
            s = S[i][j]
            D[s] += 1
        if D["x"] == 0:
            ans = min(ans, D["."])
        if K < W:
            for j in range(K, W):
                s1 = S[i][j-K]
                s2 = S[i][j]
                D[s1] -= 1
                D[s2] += 1
                if D["x"] == 0:
                    ans = min(ans, D["."])

if ans == 10 ** 6:
    print(-1)
else:
    print(ans)