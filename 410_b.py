N, Q = map(int, input().split())
X = list(map(int, input().split()))

Box = [0 for _ in range(N)]
Ball = [0 for _ in range(Q)]

for t in range(Q):
    if X[t] >= 1:
        Ball[t] = X[t]
        Box[X[t] - 1] += 1
    else:
        num = -1
        count = 1000
        for i in range(N):
            if Box[i] < count:
                num = i
                count = Box[i]
        Ball[t] = num + 1
        Box[num] += 1

print(*Ball)