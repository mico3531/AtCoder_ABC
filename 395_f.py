N, X = map(int,input().split())
U = [0 for _ in range(N)]
D = [0 for _ in range(N)]
for i in range(N):
    u, d = map(int,input().split())
    U[i] = u
    D[i] = d

print(U)

H = U[0] + D[0]
for i in range(N):
    H = min(H, U[i] + D[i])

print(H)

cost = 0
for i in range(N):
    cost += U[i] + D[i] - H
    if U[i] > H:
        U[i] = H

print(U, cost)

for i in range(1, N):
    if U[i] - U[i-1] > X:
        cost += U[i] - U[i-1] - X
        U[i] = U[i-1] + X

for i in range(N-2, -1, -1):
    if U[i] > U[i+1] + X:
        cost += U[i] - U[i+1] - X
        U[i] = U[i+1] + X

print(U)
print(cost)