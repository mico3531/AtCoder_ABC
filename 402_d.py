N, M = map(int, input().split())

num = 0
Count = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    i = (a+b) % N
    if Count[i] == 0:
        num += 1
    Count[(a+b) % N] += 1

if num == 1:
    print(0)
else:
    ans_1 = 0
    ans_2 = 0
    for i in range(N):
        ans_1 += Count[i]
        ans_2 += Count[i] ** 2
    ans = ans_1 ** 2 - ans_2
    ans //= 2
    print(ans)