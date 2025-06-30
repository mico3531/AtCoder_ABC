N = int(input())
P = list(map(int,input().split()))

r = 1
ans = [0 for _ in range(N)]
while min(ans) == 0:
    max_score = max(P)
    count = 0
    for i in range(N):
        if P[i] == max_score:
            ans[i] = r
            P[i] = 0
            count += 1
    r += count

for i in range(N):
    print(ans[i])