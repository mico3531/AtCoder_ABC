N = int(input())

A = [dict() for _ in range(N)]

P_dic = dict()
for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int,input().split())
        A[i][p] = e
        if p not in P_dic:
            P_dic[p] = [0, e]
        else:
            P_dic[p].append(e)

for p in P_dic.keys():
    P_dic[p].sort(reverse = True)

# print(A)
# print(P_dic)

LCM_used = False
ans = 0

for i in range(N):
    check = False
    for p in A[i].keys():
        if A[i][p] == P_dic[p][0] and P_dic[p][0] != P_dic[p][1]:
            check = True
    if check:
        ans += 1
    elif not LCM_used:
        ans += 1
        LCM_used = True

print(ans)