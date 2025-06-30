N, S = map(int,input().split())
A = list(map(int,input().split()))

S1 = S % sum(A)
S2 = sum(A) - S1
# print(S1, S2)

check = False

if S1 == 0:
    check = True

if not check:
    count = 0
    j = 0
    for i in range(N):
        count += A[i]
        while count > S1:
            count -= A[j]
            j += 1
        if count == S1:
            check = True

if not check:
    count = 0
    j = 0
    for i in range(N):
        count += A[i]
        while count > S2:
            count -= A[j]
            j += 1
        if count == S2:
            check = True

if check:
    print("Yes")
else:
    print("No")