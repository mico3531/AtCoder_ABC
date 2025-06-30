N = int(input())
A = list(map(int, input().split()))

ans = 0
for x in range(N+1):
    count = 0
    for i in range(N):
        if A[i] >= x:
            count += 1
    if count >= x:
        ans = x

print(ans)