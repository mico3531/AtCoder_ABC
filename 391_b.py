N, M = map(int,input().split())

S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

T = ["" for _ in range(M)]
for j in range(M):
    T[j] = str(input())

ans = []
for a in range(N-M+1):
    for b in range(N-M+1):
        check = True
        for i in range(M):
            for j in range(M):
                if S[a+i][b+j] != T[i][j]:
                    check = False
        if check:
            ans = [a+1, b+1]

print(*ans)