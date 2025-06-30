N = int(input())
Ls = [
    [[0, 0, 0] for _ in range(3 ** (N-i-1))]
    for i in range(N)]

A = str(input())
for i in range(3 ** (N-1)):
    S = A[3*i : 3*i + 3]
    if S == "000":
        Ls[0][i] = [0, 2, 0]
    elif S == "001" or S == "010" or S == "100":
        Ls[0][i] = [0, 1, 0]
    elif S == "011" or S == "101" or S == "110":
        Ls[0][i] = [1, 0, 1]
    else:
        Ls[0][i] = [2, 0, 1]

for i in range(1, N):
    for j in range(3**(N-i-1)):
        cost_0 = []
        cost_1 = []
        num = 0
        for k in range(3*j, 3*j + 3):
            cost_0.append(Ls[i-1][k][0])
            cost_1.append(Ls[i-1][k][1])
            num += Ls[i-1][k][2]
        cost_0.sort()
        Ls[i][j][0] = cost_0[0] + cost_0[1]
        cost_1.sort()
        Ls[i][j][1] = cost_1[0] + cost_1[1]
        if num >= 2:
            Ls[i][j][2] = 1

# for i in range(N):
#     print(Ls[i])

if Ls[N-1][0][2] == 0:
    print(Ls[N-1][0][1])
else:
    print(Ls[N-1][0][0])