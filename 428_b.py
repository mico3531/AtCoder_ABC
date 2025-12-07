N, K = map(int, input().split())
S = str(input())

str_dict = dict()
max_count = 1

for i in range(N-K+1):
    if S[i:i+K] not in str_dict:
        str_dict[S[i:i+K]] = 1
    else:
        str_dict[S[i:i+K]] += 1
        max_count = max(max_count, str_dict[S[i:i+K]])

# print(str_dict)
ans_ls = []
for substr in str_dict:
    if str_dict[substr] == max_count:
        ans_ls.append(substr)

ans_ls.sort()
print(max_count)
print(*ans_ls)