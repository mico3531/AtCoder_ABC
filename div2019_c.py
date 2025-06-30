N = int(input())

BA_str = 0
XA_str = 0
BX_str = 0
ans = 0
for i in range(N):
    S = str(input())
    for j in range(len(S)-1):
        if S[j] == "A" and S[j+1] == "B":
            ans += 1
    if S[0] == "B" and S[-1] == "A":
        BA_str += 1
    elif S[0] == "B":
        BX_str += 1
    elif S[-1] == "A":
        XA_str += 1

if BA_str == 0:
    ans += min(BX_str, XA_str)
else:
    if BX_str + XA_str > 0:
        ans += BA_str
        ans += min(BX_str, XA_str)
    else:
        ans += BA_str - 1
print(ans)