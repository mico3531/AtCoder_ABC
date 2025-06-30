N = int(input())
X = [0 for _ in range(N)]
H = [0 for _ in range(N)]

for i in range(N):
    X[i], H[i] = map(int,input().split())

ans = -1
for i in range(N-1):
    h = H[i] * X[i+1] - H[i+1] * X[i]
    if h >= 0:
        ans = max(h/(X[i+1]-X[i]), ans)

print(ans)