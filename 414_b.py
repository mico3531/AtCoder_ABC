N = int(input())

str_len = 0
Ls_c = ["" for _ in range(N)]
Ls_num = [0 for _ in range(N)]
for i in range(N):
    c, l = map(str, input().split())
    Ls_c[i] = c
    Ls_num[i] = int(l)
    str_len += int(l)

if str_len > 100:
    print("Too Long")
else:
    ans = ""
    for i in range(N):
        ans += Ls_c[i] * Ls_num[i]
    print(ans)