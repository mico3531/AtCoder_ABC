N, R = map(int, input().split())
L = list(map(int, input().split()))

left_data = L[:R]
left_data.reverse()
right_data = L[R:]
# print(left_data, right_data)

ans = 0

if len(left_data) > 0:
    left_press = []
    num = left_data[0]
    count = 1
    for i in range(1, len(left_data)):
        if left_data[i] == num:
            count += 1
        else:
            left_press.append([num, count])
            num = left_data[i]
            count = 1
    left_press.append([num, count])
    if left_press[-1][0] == 1:
        left_press.pop(-1)
    for data in left_press:
        if data[0] == 0:
            ans += data[1]
        else:
            ans += 2 * data[1]

if len(right_data) > 0:
    right_press = []
    num = right_data[0]
    count = 1
    for i in range(1, len(right_data)):
        if right_data[i] == num:
            count += 1
        else:
            right_press.append([num, count])
            num = right_data[i]
            count = 1
    right_press.append([num, count])
    if right_press[-1][0] == 1:
        right_press.pop(-1)
    for data in right_press:
        if data[0] == 0:
            ans += data[1]
        else:
            ans += 2 * data[1]

print(ans)