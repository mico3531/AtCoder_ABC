N, Q = map(int,input().split())
S = str(input())

cnt = 0
for i in range(N):
    if S[i] ==  "/":
        cnt += 1
ind = [-1 for _ in range(cnt)]
j = 0
for i in range(N):
    if S[i] == "/":
        ind[j] = i
        j += 1

print(ind)
for x in range(Q):
    L, R = map(int,input().split())