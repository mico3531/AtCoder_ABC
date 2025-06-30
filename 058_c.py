N = int(input())

Ansls = [100 for _ in range(26)]
for i in range(N):
    Ls = [0 for _ in range(26)]
    S = str(input())
    for j in range(len(S)):
        t = ord(S[j]) - ord("a")
        Ls[t] += 1
    for k in range(26):
        Ansls[k] = min(Ansls[k], Ls[k])

alps = [chr(ord("a") + i) for i in range(26)]
ans = ""
for i in range(26):
    ans = ans + alps[i] * Ansls[i]

print(ans)