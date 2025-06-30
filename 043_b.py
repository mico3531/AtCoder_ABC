S = str(input())
ans = ""

for i in range(len(S)):
    if S[i] == "1":
        ans = ans + "1"
    elif S[i] == "0":
        ans = ans + "0"
    elif S[i] == "B" and len(ans) != 0:
        ans = ans[:-1]

print(ans)