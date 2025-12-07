N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
d = Y - X

able = True
for i in range(1, N):
    if ( X * A[i] - X * A[0] ) % d != 0:
        able = False

if A[0] * Y < A[N-1] * X:
    able = False

if able:
    ans = 0
    mass = A[0] * Y
    for i in range(N):
        ans += (mass - A[i] * X) // (Y-X)
    print(ans)
else:
    print(-1)