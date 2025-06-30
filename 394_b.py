N = int(input())

Ls_s = [[] for _ in range(N)]
for i in range(N):
    S = str(input())
    Ls_s[i] = [len(S), S]

Ls_s.sort()
# print(Ls_s)
ans = ""
for i in range(N):
    ans = ans + Ls_s[i][1]
print(ans)