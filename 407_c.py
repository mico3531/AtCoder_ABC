S = str(input())
N = len(S)

ans = 0
for i in range(N-1):
    x = int(S[i])
    y = int(S[i+1])
    ans += 1
    t = x-y
    if t < 0:
        t += 10
    ans += t
ans += 1 + int(S[-1])
print(ans)