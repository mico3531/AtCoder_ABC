N = int(input())
A = list(map(int,input().split()))

ans = "Yes"

for i in range(1, N):
    if A[i-1] >= A[i]:
        ans = "No"

print(ans)