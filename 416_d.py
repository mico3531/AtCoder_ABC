def solve(N, M, A, B):
    A.sort()
    B.sort()
    L = 0
    R = N-1
    ret = 0
    for i in range(N):
        if A[i] + B[R] >= M:
            ret += A[i] + B[R] - M
            R -= 1
        else:
            ret += A[i] + B[L]
            L += 1
    return ret

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = solve(N, M, A, B)
    print(ans)