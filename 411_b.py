N = int(input())
D = list(map(int, input().split()))

X = [0 for _ in range(N)]
for i in range(1, N):
    X[i] = X[i-1] + D[i-1]
# print(X)

for i in range(N-1):
    Ans = [X[i+j] - X[i] for j in range(1, N-i)]
    print(*Ans)