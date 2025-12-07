S = str(input())

N = len(S)
Ls = []
alp = S[0]
num = 1

if N >= 2:
    for i in range(1, N):
        if S[i] == alp:
            num += 1
        else:
            Ls.append([alp, num])
            alp = S[i]
            num = 1
Ls.append([alp, num])

# print(Ls)

M = len(Ls)
ans = 0
if M >= 2:
    for j in range(1, M):
        x = int(Ls[j-1][0])
        x_num = Ls[j-1][1]
        y = int(Ls[j][0])
        y_num = Ls[j][1]
        if x+1 == y:
            ans += min(x_num, y_num)

print(ans)