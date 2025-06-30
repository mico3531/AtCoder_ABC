import bisect

R = int(input())
Rad_ls = [(j + 1/2) ** 2 for j in range(R+1)]
Rad_ls[0] = 0
# print(Rad_ls)

ans = 0
for i in range(R):
    border = R ** 2 - (i + 1/2) ** 2
    ind = bisect.bisect_left(Rad_ls, border)
    # print(border, ind)
    if i == 0:
        ans += (2*ind - 1)
    else:
        ans += 2 * (2*ind - 1)

print(ans)