from collections import deque

Queue = deque([])

Q = int(input())

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        c = Query[1]
        x = Query[2]
        Queue.append([x, c])
    else:
        k = Query[1]
        num = 0
        while k > 0:
            count = Queue.popleft()
            x = count[0]
            c = count[1]
            if c > k:
                num += k*x
                c -= k
                k = 0
                Queue.appendleft([x, c])
            else:
                k -= c
                num += c*x
        print(num)
    # print(Queue)