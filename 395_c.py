N = int(input())
A = list(map(int,input().split()))

ans = 10 ** 10
Num_ind = [-1 for _ in range(1 + 10**6)]
for i in range(N):
    a = A[i]
    if Num_ind[a] != -1:
        long = i - Num_ind[a] + 1
        ans = min(ans, long)
    Num_ind[a] = i

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)