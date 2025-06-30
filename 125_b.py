N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

Dif = [V[i] - C[i] for i in range(N)]

ans = 0
for i in range(N):
    if Dif[i] > 0:
        ans += Dif[i]

print(ans)