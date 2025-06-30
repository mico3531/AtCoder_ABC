H, W = map(int,input().split())

ls = []
for i in range(H):
    S = str(input())
    ls.append(S)

dels = []

for i in range(H):
    check = True
    for j in range(W):
        if ls[i][j] != ".":
            check = False
            break
    if check == True:
        dels.append(i)

dels.sort(reverse=True)
for i in dels:
    del ls[i]

dels2 = []
for j in range(W):
    check = True
    for i in range(len(ls)):
        if ls[i][j] != ".":
            check = False
            break
    if check == True:
        dels2.append(j)

dels2.sort(reverse=True)
for i in range(len(ls)):
    S = ls[i]
    for j in dels2:
        S = S[:j] + S[j+1:]
    ls[i] = S

for i in range(len(ls)):
    print(ls[i])