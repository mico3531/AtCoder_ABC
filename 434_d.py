N = int(input())

size = 2000

Sky_1 = [[0 for _ in range(size+2)] for _ in range(size+2)]
Sky_2 = [[0 for _ in range(size+2)] for _ in range(size+2)]

U = [0 for _ in range(N)]
D = [0 for _ in range(N)]
L = [0 for _ in range(N)]
R = [0 for _ in range(N)]

for i in range(N):
    U[i], D[i], L[i], R[i] = list(map(int, input().split()))
    Sky_1[U[i]][L[i]] += 1
    Sky_1[U[i]][R[i] + 1] -= 1
    Sky_1[D[i] + 1][L[i]] -= 1
    Sky_1[D[i] + 1][R[i] + 1] += 1

for i in range(size+2):
    for j in range(1, size+2):
        Sky_1[i][j] += Sky_1[i][j-1]

for j in range(size+2):
    for i in range(1, size+2):
        Sky_1[i][j] += Sky_1[i-1][j]

blank_count = 0
for i in range(1, size+1):
    for j in range(1, size+1):
        if Sky_1[i][j] == 1:
            Sky_2[i][j] = 1
        elif Sky_1[i][j] == 0:
            blank_count += 1

for i in range(size+2):
    for j in range(1, size+2):
        Sky_2[i][j] += Sky_2[i][j-1]

for j in range(size+2):
    for i in range(1, size+2):
        Sky_2[i][j] += Sky_2[i-1][j]

for i in range(N):
    u, d, l, r = U[i], D[i], L[i], R[i]
    diff = Sky_2[d][r] - Sky_2[u-1][r] - Sky_2[d][l-1] + Sky_2[u-1][l-1]
    print(blank_count + diff)