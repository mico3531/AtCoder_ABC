N, T = map(int,input().split())
lst = list(map(int,input().split()))

ans = 0
for i in range(1, N):
    ans += min(T, lst[i] - lst[i-1])
ans += T

print(ans)