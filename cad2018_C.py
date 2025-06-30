import math

N, P = map(int,input().split())

Ls = []
K = math.ceil(math.sqrt(P))+1
for d in range(2, K+1):
    while P % d == 0:
        Ls.append(d)
        P //= d
if P != 1:
    Ls.append(P)
# print(Ls)

ans = 1
S_p = set(Ls)
for x in S_p:
    count = 0
    for y in Ls:
        if x == y:
            count += 1
    count //= N
    ans *= x**count
print(ans)