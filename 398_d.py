N, R, C = map(int,input().split())
S = str(input())

large_num = 10 ** 10
posi_set = set([0])
Ans_ls = ["0" for _ in range(N)]
dist = [0,0]
for i in range(N):
    a, b = 0, 0
    if S[i] == "N":
        a -= 1
    elif S[i] == "S":
        a += 1
    elif S[i] == "W":
        b -= 1
    else:
        b += 1 
    posi_set.add((dist[0] - a) * large_num + (dist[1] - b))
    if (R - a) * large_num + (C - b) in posi_set:
        Ans_ls[i] = "1"
    dist[0] -= a
    dist[1] -= b
    R -= a
    C -= b

print("".join(Ans_ls))