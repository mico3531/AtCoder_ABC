import math

N = int(input())
A = list(map(int,input().split()))
A.sort()
# print(A)

x = -1
count = 0
for i in range(N):
    if A[i] != x:
        x = A[i]
    else:
        count += 1

if count % 2 == 1:
    count += 1
print(N-count)