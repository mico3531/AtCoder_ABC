S = str(input())
N = len(S)

ans = ""

for i in range(0, N, 2):
    ans += S[i]

print(ans)