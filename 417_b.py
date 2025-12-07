N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for x in B:
    if x in A:
        A.remove(x)

if len(A) != 0:
    print(*A)