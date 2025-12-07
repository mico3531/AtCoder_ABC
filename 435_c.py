N = int(input())
A = list(map(int, input().split()))

r_max = A[0]
ans = 1
for i in range(1, N):
    if i < r_max:
        ans += 1
        r_max = max(r_max, i + A[i])

print(ans)