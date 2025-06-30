N = int(input())

Ls = [[] for _ in range(N)]

for i in range(N):
    A, B = map(int,input().split())
    Ls[i] = [B, A]

Ls.sort()

ans = "Yes"
time = 0
for i in range(N):
    time += Ls[i][1]
    if time > Ls[i][0]:
        ans = "No"

print(ans)