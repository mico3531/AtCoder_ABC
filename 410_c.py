N, Q = map(int, input().split())

A = [i + 1 for i in range(N)]
slide = 0

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        p = Query[1] - 1
        x = Query[2]
        ind = (p + slide) % N
        A[ind] = x
    elif Query[0] == 2:
        p = Query[1] - 1
        ind = (p + slide) % N
        print(A[ind])
    else:
        k = Query[1]
        slide += k