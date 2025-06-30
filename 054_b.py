N, M = map(int,input().split())

A = ["" for _ in range(N)]
for i in range(N):
    A[i] = str(input())

B = ["" for _ in range(M)]
for j in range(M):
    B[j] = str(input())

ans = "No"
for k in range(N-M+1):
    for l in range(N-M+1):
        check = True
        for x in range(M):
            for y in range(M):
                if A[x+k][y+l] != B[x][y]:
                    check = False
        if check:
            ans = "Yes"

print(ans)