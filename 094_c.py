N = int(input())
X = list(map(int,input().split()))
Y = list(X)
Y.sort()

l = Y[-1 + N // 2]
r = Y[N // 2]
# print(l, r)

for i in range(N):
    if X[i] <= l:
        print(r)
    else:
        print(l)
