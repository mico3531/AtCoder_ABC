N, M = map(int, input().split())

S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

count = [0 for _ in range(N)]
for j in range(M):
    x = 0
    y = 0
    for i in range(N):
        if S[i][j] == "0":
            x += 1
        else:
            y += 1

    if x == 0:
        win = "1"
    elif y == 0:
        win = "0"
    elif x < y:
        win = "0"
    else:
        win = "1"

    for i in range(N):
        if S[i][j] == win:
            count[i] += 1

Ls = []
max_score = max(count)

for i in range(N):
    if count[i] == max_score:
        Ls.append(i + 1)

print(*Ls)