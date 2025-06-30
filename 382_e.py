N, X = map(int,input().split())

P = list(map(int,input().split()))
for i in range(N):
    P[i] /= 100

Single = [0 for _ in range(N+1)]
Single[0] = 1-P[0]
Single[1] = P[0]

for i in range(1, N):
    p = P[i]
    q = 1-p
    for j in range(N, 0, -1):
        Single[j] = Single[j] * q + Single[j-1] * p
    Single[0] = Single[0] * q

f = [1 for _ in range(X+1)]
f[0] = 0
for i in range(1, X+1):
    for j in range(1, N+1):
        if i-j > 0:
            f[i] += f[i-j]*Single[j]
    f[i] /= (1-Single[0])

# print(Single)
print(f[-1])