N, K = map(int,input().split())

Pair = [[0,0] for _ in range(N)]
for i in range(N):
    a, b = map(int,input().split())
    Pair[i] = [a, b]

Pair.sort()

count = 0
for i in range(N):
    count += Pair[i][1]
    if count >= K:
        ans = Pair[i][0]
        break
print(ans)