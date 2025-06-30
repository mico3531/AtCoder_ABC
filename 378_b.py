N = int(input())

Quo = [0 for _ in range(N)]
Rem = [0 for _ in range(N)]
for i in range(N):
    q, r  = map(int,input().split())
    Quo[i] = q
    Rem[i] = r

Q = int(input())
for j in range(Q):
    t, d = map(int,input().split())
    q = Quo[t-1]
    r = Rem[t-1]
    k = (d // q) - 1
    ans = k * q + r
    while ans < d:
        ans += q
    print(ans)
