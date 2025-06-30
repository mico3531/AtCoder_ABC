import bisect

N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))
Query_ls = [[] for _ in range(Q)]

for j in range(Q):
    r, x = map(int,input().split())
    Query_ls[j] = [r, x, j]
Query_ls.sort()

Ans_ls = [0 for _ in range(Q)]
LTS = [10 ** 10 for _ in range(N)]
j = 0
for i in range(1, N+1):
    ind = bisect.bisect_left(LTS, A[i])
    LTS[ind] = A[i]
    # print(LTS)
    while Query_ls[j][0] == i:
        x = Query_ls[j][1]
        num = Query_ls[j][2]
        ans = bisect.bisect_right(LTS, x)
        Ans_ls[num] = ans
        j += 1
        if j == Q:
            break
    if j == Q:
        break

# print(Ans_ls)
for i in range(Q):
    print(Ans_ls[i])