N = int(input())
A = list(map(int,input().split()))

Ls_sum = [0 for _ in range(N+1)]
for i in range(N):
    Ls_sum[i] += Ls_sum[i-1]
    A[i] += Ls_sum[i]
    if A[i] >= N-i-1:
        Ls_sum[i+1] += 1
        Ls_sum[-1] -= 1
        A[i] -= N-i-1
    else:
        Ls_sum[i+1] += 1
        Ls_sum[i+1+A[i]] -= 1
        A[i] = 0
    # print(Ls_sum)

print(*A)