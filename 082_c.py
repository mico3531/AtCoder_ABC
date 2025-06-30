N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 0
if N == 1:
    if A[0] != 1:
        ans += 1
else:
    x = A[0]
    count = 1
    for i in range(1, N):
        if A[i] == x:
            count += 1
        else:
            if x <= count:
                ans += (count - x)
            else:
                ans += count
            x = A[i]
            count = 1
    if x <= count:
        ans += (count - x)
    else:
        ans += count
print(ans)