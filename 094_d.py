N = int(input())
A = list(map(int,input().split()))
M_A = max(A)

dist = 10 ** 10
ans = -1
for i in range(N):
    if abs(A[i] - M_A / 2) < dist and A[i] != M_A:
        dist = abs(A[i] - M_A / 2)
        ans = A[i]

print(M_A, ans)