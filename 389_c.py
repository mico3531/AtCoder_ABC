Q = int(input())
Ls = [0 for _ in range(Q)]
i = 0
used_num = 0
used_long = 0
for _ in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        Ls[i] = Ls[i-1] + Query[1]
        i += 1
    elif Query[0] == 2:
        used_long = Ls[used_num]
        used_num += 1
    else:
        # print(Ls, Query[1] + used_num, used_long)
        ind = Query[1] + used_num - 2
        print(Ls[ind] - used_long)