N = int(input())
S = str(input())

ans = 0

for i in range(1, N):
    S1 = S[:i]
    S2 = S[i:]
    Set1 = set(S1)
    Set2 = set(S2)
    ans = max(ans, len(Set1 & Set2))

print(ans)