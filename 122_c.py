N, Q = map(int,input().split())
S = str(input())

Ls = [0 for _ in range(N)]
for i in range(1, N):
    Ls[i] = Ls[i-1]
    if S[i-1] == "A" and S[i] == "C":
        Ls[i] += 1

for j in range(Q):
    l, r = map(int,input().split())
    print(Ls[r-1] - Ls[l-1])