N, A, B, C = map(int,input().split())
L = [0 for _ in range(N)]
for i in range(N):
    L[i] = int(input())

ans = float("INF")
for t in range(4 ** N):
    ls_a = []
    ls_b = []
    ls_c = []
    for i in range(N):
        num = (t // (4**i)) % 4
        # print(t, num)
        if num == 0:
            ls_a.append(L[i])
        elif num == 1:
            ls_b.append(L[i])
        elif num == 2:
            ls_c.append(L[i])
    if len(ls_a) > 0 and len(ls_b) > 0 and len(ls_c) > 0:
        count = 0
        count += abs(sum(ls_a) - A) + 10 * (len(ls_a) - 1)
        count += abs(sum(ls_b) - B) + 10 * (len(ls_b) - 1)
        count += abs(sum(ls_c) - C) + 10 * (len(ls_c) - 1)
        ans = min(ans, count)

print(ans)