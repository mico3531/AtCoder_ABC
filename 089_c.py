N = int(input())

Num = [0, 0, 0, 0, 0]
for i in range(N):
    S = str(input())
    if S[0] == "M":
        Num[0] += 1
    elif S[0] == "A":
        Num[1] += 1
    elif S[0] == "R":
        Num[2] += 1
    elif S[0] == "C":
        Num[3] += 1
    elif S[0] == "H":
        Num[4] += 1

ans = 0
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans += Num[i] * Num[j] * Num[k]

print(ans)