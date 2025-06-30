from collections import deque

H, W = map(int, input().split())
A = [[] for _ in range(H)]
for i in range(H):
    A[i] = list(map(int, input().split()))

score = 0
for i in range(H):
    for j in range(W):
        score ^= A[i][j]
# print(score)

pat = [False for _ in range(2**(H*W))]
pat[0] = 0

Queue = deque([])
Queue.append([0, score])
ans = score
while len(Queue) > 0:
    X = Queue.popleft()
    x = X[0]
    pre_score = X[1]
    ans = max(ans, pre_score)
    
    for i in range(H-1):
        for j in range(W):
            s = i*W + j
            t = (i+1)*W + j
            if (not((x >> s)&1)) and (not((x>>t)&1)):
                y = x + 2**s + 2**t
                if not pat[y]:
                    pat[y] = True
                    score = pre_score ^ A[i][j] ^ A[i+1][j]
                    Queue.append([y, score])
    
    for i in range(H):
        for j in range(W-1):
            s = i*W + j
            t = i*W + (j+1)
            if (not((x >> s)&1)) and (not((x>>t)&1)):
                y = x + 2**s + 2**t
                if not pat[y]:
                    pat[y] = True
                    score = pre_score ^ A[i][j] ^ A[i][j+1]
                    Queue.append([y, score])

print(ans)