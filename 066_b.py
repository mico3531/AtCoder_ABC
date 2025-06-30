S = str(input())

for i in range(1, len(S)):
    S2 = S[:-i]
    L = len(S2)
    if L % 2 == 0:
        Sleft = S2[:L//2]
        Sright = S2[L//2:]
        if Sleft == Sright:
            print(L)
            break
        