N, Q = map(int,input().split())

Pig = [i for i in range(N+1)]
Count = [1 for _ in range(N+1)]
num = 0

for _ in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        p, next = Query[1], Query[2]
        now = Pig[p]
        Count[now] -= 1
        Count[next] += 1
        Pig[p] = next
        if Count[now] == 1:
            num -= 1
        if Count[next] == 2:
            num += 1
    else:
        print(num)