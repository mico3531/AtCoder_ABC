X = str(input())

count = 0
Ls = []
for i in range(len(X)):
    if X[i] == "0":
        count += 1
    else:
        Ls.append(X[i])

Ls.sort()
ans = Ls[0] + "0" * count

if len(Ls) > 1:
    for j in range(1, len(Ls)):
        ans += Ls[j]

print(ans)