N = int(input())
A = list(map(int,input().split()))

ans = "No"
for i in range(N-2):
    if A[i] == A[i+1] and A[i+1] == A[i+2]:
        ans = "Yes"

print(ans)