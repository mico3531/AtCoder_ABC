N, K, X = map(int, input().split())

S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

Ls = []
for t in range(N ** K):
    f = ""
    for _ in range(K):
        x = t % N
        f += S[x]
        t //= N
    Ls.append(f)

Ls.sort()
# print(Ls)
print(Ls[X-1])