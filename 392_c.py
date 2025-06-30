N = int(input())
P = [0] + list(map(int,input().split()))
Q = [0] + list(map(int,input().split()))

Q_inv = [0 for _ in range(N+1)]
for i in range(N+1):
    x = i
    y = Q[i]
    Q_inv[y] = x

Ans = [0 for _ in range(N+1)]
for i in range(1, N+1):
    Ans[i] = Q[P[Q_inv[i]]]

print(*Ans[1:])