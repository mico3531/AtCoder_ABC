N = int(input())
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = int(input())

A.sort()
ans = 0
count = 1
for i in range(1, N):
    if A[i] == A[i-1]:
        count += 1
    else:
        if count % 2 == 1:
            ans += 1
        count = 1
if count % 2 == 1:
    ans += 1
print(ans)