N, K = map(int,input().split())
A = [0 for _ in range(N+1)]
mod = 10 ** 9
pre_sum = 0
for i in range(N+1):
    if i < K:
        A[i] = 1
        pre_sum += A[i]
    else:
        A[i] = pre_sum
        pre_sum -= A[i-K]
        pre_sum += A[i]
    A[i] %= mod
    pre_sum %= mod

print(A[-1])