N = int(input())
A = list(map(int,input().split()))

X = [0 for _ in range(1 + 10 ** 5)]

for i in range(N):
    a = A[i]
    l = max(1, a-1)
    r = min(1 + 10 ** 5, a+2)
    for j in range(l, r):
        X[j] += 1
print(max(X))