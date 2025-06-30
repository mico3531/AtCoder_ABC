N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N+1):
    B = A[:i]
    Is_in = [False for _ in range(M+1)]
    for x in B:
        Is_in[x] = True
    all_in = True
    for j in range(1, M+1):
        if not Is_in[j]:
            all_in = False
    if not all_in:
        ans = N - len(B)

print(ans)