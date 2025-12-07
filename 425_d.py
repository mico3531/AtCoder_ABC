from collections import deque

H, W = map(int, input().split())
S = [[] for _ in range(H+2)]
S[0] = ["."] * (W+2)
for i in range(1, H+1):
    S[i] = ["."] + list(str(input())) + ["."]
S[-1] = ["."] * (W+2)

# for i in range(H+2):
#     print(S[i])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def meta_check(i, j):
    count = 0
    for t in range(4):
        if S[i+dx[t]][j+dy[t]] == "#":
            count += 1
    if count == 1:
        return True
    else:
        return False

def range_check(i, j):
    if 1 <= i and i <= H and 1 <= j and j <= W:
        return True
    else:
        return False

pre_Queue = deque([])
Queue = deque([])

def meta_add():
    while len(pre_Queue) > 0:
        point = pre_Queue.popleft()
        i = point[0]
        j = point[1]
        if S[i][j] == "." and meta_check(i, j):
            Queue.append([i, j])

def meta_and_pre_add():
    while len(Queue) > 0:
        point = Queue.popleft()
        i = point[0]
        j = point[1]
        S[i][j] = "#"
        for t in range(4):
            if range_check(i+dx[t], j+dy[t]):
                pre_Queue.append([i+dx[t], j+dy[t]])

for i in range(1, H+1):
    for j in range(1, W+1):
        pre_Queue.append([i, j])

while len(pre_Queue) > 0 or len(Queue) > 0:
    meta_add()
    meta_and_pre_add()

# for i in range(H+2):
#     print(S[i])

ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i][j] == "#":
            ans += 1

print(ans)