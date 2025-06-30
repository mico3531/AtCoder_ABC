N, K = map(int,input().split())
A = list(map(int,input().split()))

r = 0
sum = 0
ans = 0
for l in range(N):
    if l != 0:
        sum -= A[l-1]
    while r < N and sum < K:
        sum += A[r]
        r += 1
    if sum >= K:
        ans += N - r + 1

print(ans)