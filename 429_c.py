N = int(input())
A = list(map(int, input().split()))

A_dict = dict()
for x in A:
    if x in A_dict:
        A_dict[x] += 1
    else:
        A_dict[x] = 1

ans = 0
for x in A_dict:
    count = A_dict[x]
    if count >= 2:
        num = count * (count - 1) // 2
        num *= (N - count)
        ans += num

print(ans)