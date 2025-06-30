N, M = map(int, input().split())

Ls = [0 for _ in range(N+2)]
for _ in range(M):
    l, r = map(int, input().split())
    Ls[l] += 1
    Ls[r+1] -= 1

for i in range(1, N+2):
    Ls[i] += Ls[i-1]

ans = M
for i in range(1, N+1):
    ans = min(ans, Ls[i])

# print(Ls)
print(ans)