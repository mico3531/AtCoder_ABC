N = int(input())

S = [[] for _ in range(N)]
for i in range(N):
    S[i] = list(str(input()))

T = [[] for _ in range(N)]
for i in range(N):
    T[i] = list(str(input()))

size_S = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            size_S += 1

size_T = 0
u = 0
v = 0
for i in range(N):
    for j in range(N):
        if T[i][j] == "#":
            size_T += 1
            u = i
            v = j

def rotate(X):
    Y = [["" for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            Y[i][j] = X[j][N-1-i]
    return Y

if size_S != size_T:
    print("No")
else:
    for t in range(4):
        S = rotate(S)
        for i in range(N):
            for j in range(N):
                if S[i][j] == "#":
                    p = i
                    q = j
        dx = u - p
        dy = v - q
        count = 0
        for i in range(N):
            for j in range(N):
                if 0 <= i + dx and i + dx < N:
                    if 0 <= j + dy and j + dy < N:
                        if S[i][j] == T[i+dx][j+dy] and S[i][j] == "#":
                            count += 1
        if count == size_S:
            print("Yes")
            exit()
    print("No")