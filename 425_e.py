T, M = map(int, input().split())

C = [[1 for _ in range(5001)] for _ in range(5001)]

for n in range(2, 5001):
    for k in range(1, n):
        C[n][k] = C[n-1][k-1] + C[n-1][k]
        C[n][k] %= M

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    p = sum(A)
    ans = 1
    for i in range(N-1):
        ans *= C[p][A[i]]
        ans %= M
        p -= A[i]
    print(ans)