N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

num = 0
Ls = [[0,0] for _ in range(M)]
for i in range(M):
    B, C = map(int,input().split())
    Ls[i][0] = C
    Ls[i][1] = B
    num += B
Ls.sort(reverse = True)

D = [0] * min(num, N)
j = 0
B = Ls[j][1]
C = Ls[j][0]
for i in range(len(D)):
    if B == 0:
        j += 1
        B = Ls[j][1]
        C = Ls[j][0]
    D[i] = C
    B -= 1

for i in range(min(len(D), N)):
    if A[i] < D[i]:
        A[i] = D[i]

print(sum(A))