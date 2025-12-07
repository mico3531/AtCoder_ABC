import math
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

Queue = deque(range(1, M+1))
P_set = set()

for i in range(N):
    a = A[i]
    c = max(3, math.ceil(math.sqrt(A[i])))
    P_ls = []
    for j in range(2, c):
        if a % j == 0:
            P_ls.append(j)
            while a % j == 0:
                a //= j
    if a != 1:
        P_ls.append(a)
    # print("P_ls is", P_ls)
    for p in P_ls:
        if p not in P_set:
            P_set.add(p)
            size = len(Queue)
            if size > 0:
                for _ in range(size):
                    x = Queue.popleft()
                    if x % p != 0:
                        Queue.append(x)

print(len(Queue))
for x in Queue:
    print(x)