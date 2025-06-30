N, M = map(int,input().split())

S = []
C = []

for i in range(M):
    s, c = map(int,input().split())
    s -= 1
    c = str(c)
    S.append(s)
    C.append(c)

max = 10 ** N - 1
min = 0
if N != 1:
    min = 10 ** (N-1)

ans = -1
for i in range(max, min-1, -1):
    i = str(i)
    check = True
    for j in range(M):
        s = S[j]
        c = C[j]
        if i[s] != c:
            check = False
    if check == True:
        ans = i

print(ans)