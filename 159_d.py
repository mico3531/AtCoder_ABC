N = int(input())
A = list(map(int,input().split()))

ls = [0 for _ in range(N+1)]

for i in range(N):
    ls[A[i]] += 1

ans = 0
for i in range(N+1):
    ans += ls[i] * (ls[i] - 1) // 2

for i in range(N):
    k = ls[A[i]] - 1
    print(ans - k)
