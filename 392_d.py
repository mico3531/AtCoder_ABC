N = int(input())
K = [0 for _ in range(N)]
Dice = [dict() for _ in range(N)]

for i in range(N):
    Ls = list(map(int,input().split()))
    K[i] = Ls[0]
    for t in range(1, K[i] + 1):
        num = Ls[t]
        if num in Dice[i]:
            Dice[i][num] += 1
        else:
            Dice[i][num] = 1

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        prob = 0
        for num in Dice[i]:
            if num in Dice[j]:
                prob += Dice[i][num] * Dice[j][num]
        prob /= (K[i] * K[j])
        ans = max(ans, prob)

print(ans)