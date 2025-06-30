N, M = map(int,input().split())
p = 10 ** 9 + 7

if abs(N-M) > 1:
    ans = 0
elif abs(N-M) == 1:
    ans = 1
    for i in range(1, N+1):
        ans *= i
        ans %= p
    for j in range(1, M+1):
        ans *= j
        ans %= p
else:
    ans = 2
    for i in range(1, N+1):
        ans *= i*i
        ans %= p

print(ans)