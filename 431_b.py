X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

wearing = [False for _ in range(N)]
ans = X

for _ in range(Q):
    P = int(input())
    P -= 1
    if wearing[P]:
        ans -= W[P]
        wearing[P] = False
    else:
        ans += W[P]
        wearing[P] = True
    print(ans)