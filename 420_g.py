X = int(input())
a = abs(4*X - 1)
M = int(a ** 0.5) + 10

div_set = set()
for p in range(1, M):
    if a % p == 0:
        div_set.add(p)
        div_set.add(-p)
        q = a // p
        div_set.add(q)
        div_set.add(-q)
# print(div_set)

Ls = []
for p in div_set:
    q = (4*X - 1) // p
    s = p + q
    t = q - p - 2
    # print(s, t)
    if s % 4 == 0 and t % 4 == 0 and s >= 0:
        Ls.append(t // 4)

Ls.sort()
print(len(Ls))
print(*Ls)