N = int(input())
A = list(map(int,input().split()))

R = N // 2
L = 0

while R - L >= 2:
    mid = (R+L) // 2
    check = True
    for i in range(mid):
        ind_left = i
        ind_right = N-mid+i
        if A[ind_left] * 2 > A[ind_right]:
            check = False
            break
    if check:
        L = mid
    else:
        R = mid

# print(L, R)
check = True
for i in range(R):
    ind_left = i
    ind_right = N-R+i
    if A[ind_left] * 2 > A[ind_right]:
        check = False
        break

# print(L, R, check)

if check:
    print(R)
else:
    print(L)