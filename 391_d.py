N, W = map(int,input().split())

Col = [[] for _ in range(W)]
for i in range(1, N+1):
    x, y = map(int,input().split())
    Col[x-1].append([y, i])

for i in range(W):
    Col[i].sort()

num_del = N
for i in range(W):
    num_del = min(num_del, len(Col[i]))

# print(num_del)

time_del = [10 ** 10 for _ in range(N+1)]
a = 0
for i in range(num_del):
    for j in range(W):
        a = max(a, Col[j][i][0])
    for j in range(W):
        ind = Col[j][i][1]
        time_del[ind] = a
    a += 1

Q = int(input())
for _ in range(Q):
    T, A = map(int,input().split())
    if time_del[A] < T + 0.5:
        print("No")
    else:
        print("Yes")