N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)

if sum_A - M in A:
    print("Yes")
else:
    print("No")