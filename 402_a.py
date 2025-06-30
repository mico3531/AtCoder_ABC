S = str(input())
ans = ""
for i in range(len(S)):
    if S[i].isupper():
        ans += S[i]

print(ans)