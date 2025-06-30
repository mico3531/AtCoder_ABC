Q = int(input())
count = 0
Ls = []
for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        x = Query[1]
        Ls.append(x)
    else:
        count += 1

for i in range(count):
    print(Ls[i])