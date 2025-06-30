N = int(input())
H = list(map(int,input().split()))

M = max(H)
ans = 0
for i in range(1, M+1):
    if H[0] >= i:
        check = True
    else:
        check = False
    for j in range(N):
        if H[j] >= i and check == False:
            check = True
        elif H[j] < i and check == True:
            check = False
            ans += 1
    if check == True:
        ans += 1

print(ans)