import bisect

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    ind = bisect.bisect_left(A, 2 * A[i])
    # print(ind, N-ind)
    ans += N-ind

print(ans)