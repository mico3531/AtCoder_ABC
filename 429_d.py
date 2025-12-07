N, M, C = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

press_A = [[-1,0]]
for x in A:
    if x != press_A[-1][0]:
        num = press_A[-1][1]
        press_A.append([x, num + 1])
    else:
        press_A[-1][1] += 1

press_A.pop(0)
# print(press_A)

K = len(press_A)
for i in range(K):
    data = press_A[i]
    x = data[0]
    num = data[1]
    press_A.append([x + M, num + N])

press_A.append([10**10, 10**10])

# print(press_A)

ans = 0
for i in range(K):
    area = press_A[i+1][0] - press_A[i][0]
    num = press_A[i][1]
    l = 0
    r = 2*K
    # print("search", num + C)
    while r-l > 1:
        m = (l+r) // 2
        if press_A[m][1] >= num + C:
            r = m
        else:
            l = m
    # print(l, r)
    ans += area * (press_A[r][1] - press_A[i][1])

print(ans)