H, W = map(int,input().split())
ls = []
for _ in range(H):
    S = str(input())
    ls.append(S)

ans = "Yes"
for i in range(H):
    for j in range(W):
        if ls[i][j] == "#":
            check = False
            for k in [i-1, i+1]:
                if k in range(H):
                    if ls[k][j] == "#":
                        check = True
            for l in [j-1, j+1]:
                if l in range(W):
                    if ls[i][l] == "#":
                        check = True
            if check == False:
                ans = "No"

print(ans)