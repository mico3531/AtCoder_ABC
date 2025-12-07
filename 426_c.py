N, Q = map(int, input().split())

count = [1 for _ in range(N+1)]
count[0] = 0

for _ in range(Q):
    X, Y = map(int, input().split())
    ans = 0
    while count[X] > 0:
        ans += count[X]
        count[Y] += count[X]
        count[X] = 0
        X -= 1
    print(ans)