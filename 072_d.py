N = int(input())

P = [0] + list(map(int,input().split()))

ans = 0

for i in range(1, N):
    if i == P[i]:
        x = P[i]
        y = P[i+1]
        P[i] = y
        P[i+1] = x
        ans += 1

if P[N] == N:
    ans += 1

print(ans)