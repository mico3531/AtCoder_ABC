a, b, c, d = map(int,input().split())

Ls = [0 for _ in range(5)]
Ls[a] += 1
Ls[b] += 1
Ls[c] += 1
Ls[d] += 1

ans = 0
for i in range(1, 5):
    ans += Ls[i] // 2

print(ans)