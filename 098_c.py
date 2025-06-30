N = int(input())
S = str(input())

if N == 2:
    if S == "WE":
        ans = 1
    else:
        ans = 0

Froml = [0 for _ in range(N)]
for i in range(1, N):
    Froml[i] = Froml[i-1]
    if S[i-1] == "E":
        Froml[i] += 1

Fromr = [0 for _ in range(N)]
for i in range(N-2, -1, -1):
    Fromr[i] = Fromr[i+1]
    if S[i+1] == "W":
        Fromr[i] += 1

Sumls = [Froml[i] + Fromr[i] for i in range(N)]
if N != 2:
    ans = N - max(Sumls) - 1
print(ans)