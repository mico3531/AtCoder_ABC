S = str(input())

Ls = []
for i in range(len(S)):
    if S[i] == "#":
        Ls.append(i+1)

for j in range(len(Ls) // 2):
    print(str(Ls[2*j]) + "," + str(Ls[2*j + 1]))