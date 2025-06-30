N = int(input())
L = [0 for _ in range(N)]
R = [0 for _ in range(N)]
for i in range(N):
    L[i], R[i] = map(int,input().split())

Q = int(input())
Ls_query = [0 for _ in range(Q)]
for j in range(Q):
    Ls_query[j] = int(input())

Ls = [0 for _ in range(N + Q + 1)]