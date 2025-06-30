N = int(input())
A = list(map(int,input().split()))
S = sum(A)

T1 = A[0]
T2 = S - A[0]
ans = abs(T1-T2)

T1 = 0
T2 = S
for i in range(N-1):
    T1 += A[i]
    T2 -= A[i]
    if abs(T1-T2) < ans:
        ans = abs(T1-T2)

print(ans)