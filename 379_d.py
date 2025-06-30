from collections import deque

Q = int(input())
A = [0 for _ in range(Q+1)]
q = deque()

for i in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        # print("plant")
        A[i] = A[i-1]
        q.append(i)
    elif Query[0] == 2:
        # print("glow")
        A[i] = A[i-1] + Query[1]
    else:
        c = 0
        # print("Cut")
        A[i] = A[i-1]
        while len(q) > 0 and A[i-1] - A[q[0]] >= Query[1]:
            x = q.popleft()
            c += 1
        print(c)