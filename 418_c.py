import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

S = [0 for _ in range(N)]
for i in range(1, N):
    S[i] = S[i-1] + A[i-1]

for _ in range(Q):
    B = int(input())
    if B > A[-1]:
        ans = -1
    else:
        ind = bisect.bisect_left(A, B)
        ans = 1
        ans += S[ind]
        ans += (B-1) * (N - ind)
    print(ans)