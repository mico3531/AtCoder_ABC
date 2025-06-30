N = int(input())
A = list(map(int,input().split()))

A.sort()

same = []

i = 1
while i < N:
    if A[i-1] == A[i]:
        same.append(A[i])
        i += 1
    i += 1

same.sort(reverse=True)

if len(same) >= 2:
    print(same[0] * same[1])
else:
    print(0)
