S = str(input())
Q = int(input())

mir = False

Tasks = [[] for _ in range(Q)]
for i in range(Q):
    Query = list(map(str,input().split()))
    Tasks[i] = Query

pre = 0
suf = 0
mir = False
for i in range(Q):
    Query = Tasks[i]
    if Query[0] == "1":
        mir = not mir
    else:
        if Query[1] == "1":
            if mir:
                suf += 1
            else:
                pre += 1
        else:
            if mir:
                pre += 1
            else:
                suf += 1

# print(pre, S, suf)

ans = ["" for _ in range(pre + suf + 1)] 
ans[pre] = S
L = pre - 1
R = pre + 1
# print(ans)

mir = False
for i in range(Q):
    Query = Tasks[i]
    if Query[0] == "1":
        mir = not mir
    else:
        if Query[1] == "1":
            if mir:
                ans[R] = Query[2]
                R += 1
            else:
                ans[L] = Query[2]
                L -= 1
        else:
            if mir:
                ans[L] = Query[2]
                L -= 1
            else:
                ans[R] = Query[2]
                R += 1
        # print(ans)

# print(ans)

T = "".join(ans)

if mir:
    print(T[::-1])
else:
    print(T)