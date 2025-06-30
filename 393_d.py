N = int(input())
S = str(input())

ind_1 = set()
for i in range(N):
    if S[i] == "1":
        ind_1.add(i)

Ls_1 = sorted(list(ind_1))
# print(Ls_1)
L = len(Ls_1)
cent_ind = L//2
cent_num = Ls_1[L//2]

ans = 0
for j in range(L):
    dest = cent_num + (j - cent_ind)
    ans += abs(dest - Ls_1[j])
    # print(dest)

print(ans)