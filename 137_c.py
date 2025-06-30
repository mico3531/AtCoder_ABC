N = int(input())

Ls = ["" for _ in range(N)]
for i in range(N):
    Sls = sorted(str(input()))
    S = "".join(Sls)
    Ls[i] = S

Ls.sort()
# print(Ls)

ans = 0
count = 1
S = Ls[0]
for i in range(1, N):
    if S == Ls[i]:
        count += 1
    else:
        ans += count * (count - 1) // 2
        count = 1
        S = Ls[i]
ans += count * (count - 1) // 2

print(ans)