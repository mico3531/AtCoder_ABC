N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if sum(A) <= K:
    for i in range(N):
        ans += A[i] * (A[i]+1) // 2
else:
    left = 0
    right = 10 ** 10
    while right - left > 1:
        count = 0
        middle = (left + right) // 2
        for i in range(N):
            if A[i] >= middle:
                count += A[i] - middle + 1
        if count <= K:
            right = middle
        else:
            left = middle
    # print(right)
    use_count = 0
    for i in range(N):
        if A[i] >= right:
            ans += A[i] * (A[i]+1) // 2
            ans -= (right-1) * (right) // 2
            use_count += A[i] - right + 1
    ans += (right - 1) * (K - use_count)
print(ans)