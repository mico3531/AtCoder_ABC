N, Q = map(int, input().split())

Querys = []
for i in range(Q):
    Ls = list(map(str, input().split()))
    Ls[0] = int(Ls[0])
    Ls[1] = int(Ls[1])
    Querys.append(Ls)

Ans_ls = []
check = 0
for i in range(Q-1, -1, -1):
    Ls = Querys[i]
    if Ls[0] == 1:
        p = Ls[1]
        if check == p:
            check = 0
    elif Ls[0] == 2:
        p = Ls[1]
        s = Ls[2]
        if check == p:
            Ans_ls.append(s)
    else:
        p = Ls[1]
        if check == 0:
            check = p

Ans_ls.reverse()
print("".join(Ans_ls))