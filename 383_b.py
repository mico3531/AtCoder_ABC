H, W, D = map(int,input().split())

S = ["" for _ in range(H)]
for i in range(H):
    S[i] = str(input())

def mand(x, y, z, w):
    return abs(x-z) + abs(y-w)

ans = 0
for x in range(H*W-1):
    for y in range(x+1, H*W):
        p1 = x // W
        p2 = x % W
        q1 = y // W
        q2 = y % W
        # print([p1, p2], [q1, q2])
        if S[p1][p2] == "." and S[q1][q2] == ".":
            count = 0
            for i in range(H):
                for j in range(W):
                    if S[i][j] == ".":
                        if mand(i, j, p1, p2) <= D or mand(i, j, q1, q2) <= D:
                            count += 1
            ans = max(ans, count)

print(ans)