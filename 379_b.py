N, K = map(int,input().split())
S = str(input())

count = 0
ans = 0
for i in range(N):
    if S[i] == "O":
        count += 1
    else:
        count = 0
    if count >= K:
        ans += 1
        count = 0

print(ans)