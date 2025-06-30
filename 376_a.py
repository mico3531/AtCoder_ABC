N, C = map(int,input().split())
T = list(map(int,input().split()))

ans = 1
past = T[0]

for i in range(1, N):
    if T[i] - past >= C:
        ans += 1
        past = T[i]

print(ans)