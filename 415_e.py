from collections import deque

H, W = map(int, input().split())

A = [[] for _ in range(H)]
for i in range(H):
    A[i] = list(map(int, input().split()))
P = list(map(int, input().split()))

left = -1
right = 10 ** 16

dp = [[0 for _ in range(W)] for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]

def check(x):
    dp[0][0] = x + A[0][0] - P[0]
    if dp[0][0] < 0:
        dp[0][0] = - 10 ** 16
    
    for i in range(1, H):
        dp[i][0] = dp[i-1][0] + A[i][0] - P[i]
        if dp[i][0] < 0:
            dp[i][0] = -10 ** 16
    
    for j in range(1, W):
        dp[0][j] = dp[0][j-1] + A[0][j] - P[j]
        if dp[0][j] < 0:
            dp[0][j] = -10 ** 16
    
    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + A[i][j] - P[i+j]
            if dp[i][j] < 0:
                dp[i][j] = -10 ** 16
    
    for i in range(H):
        for j in range(W):
            visited[i][j] = False
    
    next = deque([])
    if dp[0][0] >= 0:
        next.append([0, 0])
        visited[0][0] = True
    
    while len(next) > 0:
        t = next.popleft()
        i = t[0]
        j = t[1]
        
        if i+1 < H:
            if visited[i+1][j] == False and dp[i+1][j] >= 0:
                visited[i+1][j] = True
                next.append([i+1, j])
        
        if j+1 < W:
            if visited[i][j+1] == False and dp[i][j+1] >= 0:
                visited[i][j+1] = True
                next.append([i, j+1])
    
    # for i in range(H):
    #         print(dp[i])
    
    # for i in range(H):
    #         print(visited[i])

    return visited[H-1][W-1]
    

while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
    # print(left, right)

print(right)