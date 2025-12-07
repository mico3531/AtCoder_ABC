S = str(input())

s_ls = []
for i in range(len(S)):
    if S[i] not in s_ls:
        s_ls.append(S[i])

count = 0
for i in range(len(S)):
    if S[i] == s_ls[0]:
        count += 1

if count == 1:
    print(s_ls[0])
else:
    print(s_ls[1])