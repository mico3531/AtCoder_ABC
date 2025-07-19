N, L, R = map(int, input().split())

ans = 0
for _ in range(N):
    X, Y = map(int, input().split())
    if X <= L and R <= Y:
        ans += 1

print(ans)