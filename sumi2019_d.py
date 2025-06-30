N = int(input())
S = str(input())
L = [N+1 for _ in range(10)]
R = [-1 for _ in range(10)]

for i in range(N):
    a = int(S[i])
    L[a] = min(L[a], i)
    R[a] = max(R[a], i)

ans = 0
for a in range(10):
    for b in range(10):
        if L[a] + 2 <= R[b]:
            kind = set()
            for i in range(L[a]+1, R[b]):
                kind.add(S[i])
            ans += len(kind)
print(ans)