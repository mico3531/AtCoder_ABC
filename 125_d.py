N = int(input())
A = list(map(int,input().split()))
Ls_abs = [[abs(A[i]), A[i]] for i in range(N)]
Ls_abs.sort()

nega_count = 0
for i in range(N):
    if A[i] < 0:
        nega_count += 1

ans = 0
if nega_count % 2 == 0:
    for i in range(N):
        ans += Ls_abs[i][0]
else:
    ans -= Ls_abs[0][0]
    for i in range(1, N):
        ans += Ls_abs[i][0]

print(ans)