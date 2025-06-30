from collections import deque

N = int(input())
A = list(map(int, input().split()))

Right_more = [N for _ in range(N)]

Stack = deque([])
for i in range(N):
    while len(Stack) > 0 and A[i] > A[Stack[-1]]:
        Right_more[Stack[-1]] = i
        Stack.pop()
    Stack.append(i)
print(Right_more)

Left_more = [-1 for _ in range(N)]

Stack = deque([])
for i in range(N-1, -1, -1):
    while len(Stack) > 0 and A[i] > A[Stack[-1]]:
        Left_more[Stack[-1]] = i
        Stack.pop()
    Stack.append(i)
print(Left_more)

Ls = []