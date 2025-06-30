N, M = map(int,input().split())

P = [[] for _ in range(M)]
for i in range(M):
    a, b = map(int,input().split())
    P[i] = [a-1, b-1]

move= [[-2, -1], [-2, 1], [-1, -2], [-1, 2], 
[1, -2], [1, 2], [2, -1], [2, 1]]

S = set()

for i in range(M):
    S.add(P[i][0] + P[i][1] * N)
    for j in range(8):
        x = P[i][0] + move[j][0]
        y = P[i][1] + move[j][1]
        if 0 <= x and x <= N-1 and 0 <= y and y <= N-1:
            S.add(x + y * N)

print(N ** 2 - len(S))