N, D = map(int,input().split())
T = [0 for _ in range(N)]
L = [0 for _ in range(N)]
for i in range(N):
    T[i], L[i] = map(int,input().split())

W = [0 for _ in range(N)]
for k in range(1, D+1):
    for i in range(N):
        W[i] = T[i] * (L[i] + k)
    print(max(W))