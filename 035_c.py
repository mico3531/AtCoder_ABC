N, Q = map(int, input().split())

Ls = [0 for _ in range(N+2)]
for _ in range(Q):
    l, r = map(int, input().split())
    Ls[l] += 1
    Ls[r+1] -= 1

for i in range(1, N+2):
    Ls[i] += Ls[i-1]

Ans = [str(Ls[i] % 2) for i in range(N+2)]
print("".join(Ans[1: N+1]))