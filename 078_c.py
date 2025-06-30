N, M = map(int,input().split())

t = 1900 * M + 100 * (N-M)
p = (0.5) ** M
ans = int(t / p)
print(ans)