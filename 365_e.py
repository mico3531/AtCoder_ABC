import math

N = int(input())
A = [0] + list(map(int, input().split()))

# 30桁目まで

ans = 0

for t in range(30):
    Ls_sum = [(A[i] >> t) & 1 for i in range(N+1)]
    for i in range(1, N+1):
        Ls_sum[i] += Ls_sum[i-1]
        Ls_sum[i] %= 2
    # print(Ls_sum)
    count_0 = 0
    count_1 = 0
    for i in range(N+1):
        if Ls_sum[i] == 0:
            count_0 += 1
        else:
            count_1 += 1
    ans += count_0 * count_1 * (2**t)

print(ans - sum(A))