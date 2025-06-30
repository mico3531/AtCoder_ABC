import copy

N = int(input())
A = list(map(int,input().split()))
B = copy.deepcopy(A)
B.sort()
num = -1
if N == 1:
    num = A[0]
else:
    if B[0] != B[1]:
        num = B[0]
    if B[-1] != B[-2]:
        num = B[-1]
    for i in range(1, N-1):
        if B[i-1] != B[i] and B[i] != B[i+1]:
            num = max(B[i], num)

# print(A)
# print(B)
if num == -1:
    print(-1)
else:
    ans = A.index(num) + 1
    print(ans)