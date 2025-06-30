N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A) < sum(B):
    print(-1)
else:
    Diff = [A[i] - B[i] for i in range(N)]
    Diff.sort()
    count = 0
    ans = 0
    for i in range(N):
        if Diff[i] < 0:
            count += Diff[i]
            ans += 1
    j = N-1
    while count < 0:
        count += Diff[j]
        j -= 1
        ans += 1
    print(ans)