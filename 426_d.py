def press(S):
    ret = []
    alp = S[0]
    count = 1
    for i in range(1, len(S)):
        if S[i] == alp:
            count += 1
        else:
            ret.append([alp, count])
            count = 1
            alp = S[i]
    ret.append([alp, count])
    return ret

def solve(ls):
    N = len(ls)
    zero_count = 0
    one_count = 0
    for i in range(N):
        if ls[i][0] == "0":
            zero_count += ls[i][1]
        else:
            one_count += ls[i][1]
    
    ret = float("INF")
    for i in range(N-1):
        ans = 0
        if ls[i][0] == "0":
            new_zero = zero_count - ls[i][1]
            new_one = one_count - ls[i+1][1]
            ans += new_zero + new_one
            ans += min(new_zero + ls[i+1][1], new_one + ls[i][1])
        else:
            new_zero = zero_count - ls[i+1][1]
            new_one = one_count - ls[i][1]
            ans += new_zero + new_one
            ans += min(new_zero + ls[i][1], new_one + ls[i+1][1])
        ret = min(ret, ans)
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    S = str(input())
    ls = press(S)
    # print(ls)
    if len(ls) == 1:
        print(0)
    else:
        ans = solve(ls)
        print(ans)