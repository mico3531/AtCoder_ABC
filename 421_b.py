X, Y = map(int, input().split())

Ls = [0 for _ in range(10)]
Ls[0] = X
Ls[1] = Y
for i in range(2, 10):
    num = Ls[i-2] + Ls[i-1]
    pre_str = str(num)
    new_str = pre_str[::-1]
    # print(pre_str, new_str)
    new_num = int(new_str)
    Ls[i] = new_num

# print(Ls)
print(Ls[-1])