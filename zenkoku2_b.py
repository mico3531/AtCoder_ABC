N = int(input())
D = list(map(int,input().split()))
M = max(D)
Ls = [0 for _ in range(M+1)]

for i in range(N):
    d = D[i]
    Ls[d] += 1

# print(Ls)
m = 998244353
if D[0] == 0 and Ls[0] == 1:
    ans = 1
    if M >= 1:
        for j in range(M):
            ans *= Ls[j] ** Ls[j+1]
            ans %= m
            # print("ans is", ans)
        print(ans)
else:
    print(0)