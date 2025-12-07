N, M = map(int, input().split())

E = [[] for _ in range(M)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    E[i] = [u, v]

ans = M
for k in range(2**N):
    count = 0
    for i in range(M):
        u = E[i][0]
        v = E[i][1]
        if (k >> u) % 2 == (k >> v) % 2:
            count += 1
    ans = min(ans, count)
print(ans)