T = int(input())

for _ in range(T):
    N = int(input())
    S = str(input())
    Ls = []
    alp = S[0]
    count = 0
    for i in range(N):
        if S[i] == alp:
            count += 1
        else:
            Ls.append([alp, count])
            alp = S[i]
            count = 1
    Ls.append([alp, count])
    if Ls[0][0] == "0":
        Ls = Ls[1:]
    # print(Ls)

    X = len(Ls)
    if X == 0:
        ans = 0
    else:
        DP = [[10 ** 6, 10 ** 6, 10 ** 6] for _ in range(X)]
        DP[0] = [Ls[0][1], 0, Ls[0][1]]
        for j in range(1, X):
            if Ls[j][0] == "0":
                DP[j][0] = DP[j-1][0]
                DP[j][1] = min(DP[j-1][0], DP[j-1][1]) + Ls[j][1]
                DP[j][2] = min(DP[j-1][1], DP[j-1][2])
            else:
                DP[j][0] = DP[j-1][0] + Ls[j][1]
                DP[j][1] = min(DP[j-1][0], DP[j-1][1])
                DP[j][2] = min(DP[j-1][1], DP[j-1][2]) + Ls[j][1]
        # print(DP[-1])
        ans = min(DP[-1])
    print(ans)