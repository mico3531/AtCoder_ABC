N = int(input())
S = [["", i] for i in range(N)]
for i in range(N):
    S[i][0] = str(input())
S.sort()

Ans = [0 for _ in range(N)]

for i in range(N):
    ans = 0
    
    if i != 0:
        x = min(len(S[i-1][0]), len(S[i][0]))
        count = 0
        for j in range(x):
            if S[i-1][0][j] == S[i][0][j]:
                count += 1
            else:
                break
        ans = max(ans, count)
    
    if i != N-1:
        x = min(len(S[i][0]), len(S[i+1][0]))
        count = 0
        for j in range(x):
            if S[i][0][j] == S[i+1][0][j]:
                count += 1
            else:
                break
        ans = max(ans, count)
    
    Ans[S[i][1]] = ans

for i in range(N):
    print(Ans[i])