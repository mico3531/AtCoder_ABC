N, D = map(int,input().split())
S = str(input())

ans = 0
for i in range(N):
    if S[i] == ".":
        ans += 1

print(ans+D)