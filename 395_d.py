N, Q = map(int,input().split())

Ind = [i for i in range(N+1)]
Name = [i for i in range(N+1)]
Name_inv = [i for i in range(N+1)]

for _ in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        a = Query[1]
        b = Query[2]
        To = Name_inv[b]
        Ind[a] = To
    elif Query[0] == 2:
        a = Query[1]
        b = Query[2]
        c = Name_inv[a]
        d = Name_inv[b]
        Name_inv[a] = d
        Name_inv[b] = c
        Name[c] = b
        Name[d] = a
    else:
        a = Query[1]
        ans = Name[Ind[a]]
        print(ans)
