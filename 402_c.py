N, M = map(int, input().split())

Recipe = [[] for _ in range(M)]
for i in range(M):
    Recipe[i] = list(map(int, input().split()))

B = [0] + list(map(int, input().split()))
B_inv = [0 for _ in range(N+1)]
for x in range(N+1):
    y = B[x]
    B_inv[y] = x
# print(B_inv)

eat_day = [0 for _ in range(M)]
for i in range(M):
    K = Recipe[i][0]
    for j in range(1, K+1):
        eat_day[i] = max(eat_day[i], B_inv[Recipe[i][j]])
# print(eat_day)

Ans = [0 for _ in range(N+1)]
for i in range(M):
    Ans[eat_day[i]] += 1
for t in range(1, N+1):
    Ans[t] += Ans[t-1]
# print(Ans)

for t in range(1, N+1):
    print(Ans[t])