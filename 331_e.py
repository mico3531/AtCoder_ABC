N, M, L = map(int,input().split())
A = list(map(int,input().split()))
B_pri = list(map(int,input().split()))

B = [[B_pri[j], j] for j in range(M)]
B.sort()

# print(A)
# print(B)

NG = [set() for _ in range(N)]
for _ in range(L):
    c, d = map(int,input().split())
    NG[c-1].add(d-1)

ans = 0
for i in range(N):
    j = M-1
    while B[j][1] in NG[i]:
        j -= 1
        if j == -1:
            break
    if j != -1:
        ans = max(ans, A[i] + B[j][0])

print(ans)