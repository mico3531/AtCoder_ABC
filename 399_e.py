N = int(input())
S = str(input())
T = str(input())

trans_dict = dict()
for i in range(N):
    if S[i] not in trans_dict:
        trans_dict[S[i]] = T[i]
    elif trans_dict[S[i]] != T[i]:
        print(-1)
        exit()

if len(trans_dict) == 26:
    for s in trans_dict:
        if trans_dict[s] != s:
            print(-1)
            exit()
    print(0)
else:
    # print("OK")
    ans = 0
    count = 0
    while len(trans_dict) > 0:
        delete_set = set()
        for s in trans_dict:
            t = trans_dict[s]
            if t not in trans_dict:
                delete_set.add(s)
            elif trans_dict[t] == s:
                delete_set.add(s)
        if len(delete_set) > 0:
            for s in delete_set:
                t = trans_dict[s]
                trans_dict.pop(s)
                if s != t:
                    # print("plus", s, t)
                    ans += 1
        elif len(trans_dict) > 0:
            x = 0
            for s in trans_dict:
                if x == 0:
                    trans_dict[s] = str(count)
                    count += 1
                    x += 1
                    ans += 1
    print(ans)