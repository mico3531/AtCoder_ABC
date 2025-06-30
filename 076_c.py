import re

S = str(input())
ls = len(S)
S = S.replace("?", ".")

T = str(input())
lt = len(T)

check = False
if lt <= ls:
    for i in range(ls - lt, -1, -1):
        if re.fullmatch(S[i: i+lt], T) != None:
            check = True
            ans = S[:i] + T + S[i+lt:]
            print(ans.replace(".", "a"))
            break

if not check:
    print("UNRESTORABLE")