N, M, Q = map(int, input().split())

AC = [set() for _ in range(N+1)]

for _ in range(Q):
    Query = list(map(int, input().split()))

    if Query[0] == 1:
        x, y = Query[1], Query[2]
        if AC[x] != "all":
            AC[x].add(y)
    
    elif Query[0] == 2:
        x = Query[1]
        AC[x] = "all"
    
    else:
        x, y = Query[1], Query[2]
        if AC[x] == "all":
            print("Yes")
        elif y in AC[x]:
            print("Yes")
        else:
            print("No")