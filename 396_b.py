from collections import deque

Q = int(input())
St = deque([0 for _ in range(100)])

for _ in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        x = Query[1]
        St.append(x)
    else:
        y = St.pop()
        print(y)