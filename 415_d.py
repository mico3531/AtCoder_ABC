N, M = map(int, input().split())

Ls = [[] for _ in range(M)]
for i in range(M):
    a, b = map(int, input().split())
    Ls[i] = [a-b, a, b]
Ls.sort()
# print(Ls)

score = 0
i = 0
while i < M:
    c = Ls[i][0]
    a = Ls[i][1]
    b = Ls[i][2]
    if N >= a:
        k = (N-a) // c
        score += k
        N -= k*c
    if N >= a:
        score += 1
        N -= a
        N += b
    i += 1

print(score)