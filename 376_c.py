N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

ans = 0

for i in range(N-1):
    if A[i] > B[i]:
        ans = -1
        break

if ans != -1:
    for i in range(N-2, -1, -1):
        if B[i] < A[i+1]:
            ans = A[i+1]
            break
    if ans == 0:
        ans = A[0]

print(ans)