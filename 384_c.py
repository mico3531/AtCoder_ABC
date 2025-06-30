Ls = list(map(int,input().split()))

Ans = [[0, ""] for _ in range(32)]

for i in range(32):
    for j in range(5):
        if (i >> j) & 1:
            Ans[i][1] += chr(ord("A") + j)
            Ans[i][0] += Ls[j]

Ans = Ans[1:]
Ans = sorted(Ans, key = lambda x:x[1])
Ans = sorted(Ans, key = lambda x:x[0], reverse = True)
for i in range(31):
    print(Ans[i][1])