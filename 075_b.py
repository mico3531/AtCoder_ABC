H, W = map(int,input().split())
ls = []
for _ in range(H):
    S = str(input())
    ls.append(list(S))

for i in range(H):
    for j in range(W):
        if ls[i][j] == ".":
            ls[i][j] = int(0)

for i in range(H):
    for j in range(W):
        if ls[i][j] == "#":
            for k in range(max(i-1, 0), min(i+2, H)):
                for l in range(max(j-1, 0), min(j+2, W)):
                    if ls[k][l] != "#":
                        ls[k][l] += 1

for i in range(H):
    S = "".join(map(str, ls[i]))
    print(S)