N, Q = map(int, input().split())
A_1 = [0] + list(map(int, input().split()))
sum_A_1 = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_A_1[i] = sum_A_1[i-1] + A_1[i]

A_2 = [i * A_1[i] for i in range(N+1)]
sum_A_2 = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_A_2[i] = sum_A_2[i-1] + A_2[i]

A_3 = [i * i * A_1[i] for i in range(N+1)]
sum_A_3 = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_A_3[i] = sum_A_3[i-1] + A_3[i]

for _ in range(Q):
    L, R = map(int, input().split())
    ans = - (sum_A_3[R] - sum_A_3[L-1])
    ans += (L+R) * (sum_A_2[R] - sum_A_2[L-1])
    ans += (R - L - L*R + 1) * (sum_A_1[R] - sum_A_1[L-1])
    print(ans)