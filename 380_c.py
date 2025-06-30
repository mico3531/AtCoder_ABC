N, K = map(int,input().split())
S = str(input())

a = S[0]
T = 1
for i in range(1, N):
    if S[i] != a:
        T += 1
        a = S[i]

Ls = [[] for _ in range(T)]
a = S[0]
l = 0
r = 1
j = 0
for i in range(1, N):
    if S[i] != a:
        Ls[j] = [a, l, r]
        j += 1
        a = S[i]
        l = i
        r = i+1
    else:
        r += 1
Ls[j] = [a, l, r]
# print(Ls)

if Ls[0][0] == "0":
    x = 2*K-2
    y = 2*K-1
else:
    x = 2*K-3
    y = 2*K-2
# print(x, y)

A = Ls[x][1]
B = Ls[y][2]
ans = S[:A]
ans = ans + Ls[y][0] * (Ls[y][2] - Ls[y][1])
ans = ans + Ls[x][0] * (Ls[x][2] - Ls[x][1])
ans = ans + S[B:]
print(ans)