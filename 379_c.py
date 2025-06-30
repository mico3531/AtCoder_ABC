N, M = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))

sum = sum(A)
S = [[X[j], A[j]] for j in range(M)]
S.sort()

i = 0
ans = 0
check = True
for j in range(M):
    x = S[j][0]
    a = S[j][1]
    # print(i, a, x)
    if i+1 < x:
        check = False
        break
    else:
        ans += a * (a-1) // 2
        ans += (i+1-x) * a
        i += a
    # print(ans)

if sum != N:
    check = False

if check:
    print(ans)
else:
    print(-1)