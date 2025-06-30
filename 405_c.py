N = int(input())
A = list(map(int, input().split()))
ans = sum(A) ** 2
for i in range(N):
    ans -= A[i] ** 2
ans //= 2
print(ans)