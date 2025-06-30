N, K = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
if K % 2 == 0:
    for i in range(K):
        if i % 2 == 0:
            ans += A[i+1] - A[i]
else:
    Presum = [0 for _ in range(K)]
    for i in range(2, K):
        Presum[i] = Presum[i-1]
        if i % 2 == 0:
            Presum[i] += A[i-1] - A[i-2]
    
    Sufsum = [0 for _ in range(K)]
    for i in range(K-2, -1, -1):
        Sufsum[i] = Sufsum[i+1]
        if i % 2 == 0:
            Sufsum[i] += A[i+2] - A[i+1]
    
    Ans = [Presum[i] + Sufsum[i] for i in range(K)]
    for i in range(K):
        if i % 2 == 1:
            Ans[i] += A[i+1] - A[i-1]
    
    ans = min(Ans)

    # print(Presum)
    # print(Sufsum)
    # print(Ans)

print(ans)