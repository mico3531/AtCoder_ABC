import heapq

H, W, X = map(int,input().split())
P, Q = map(int,input().split())
P -= 1
Q -= 1

S = [[] for _ in range(H)]
for i in range(H):
    S[i] = list(map(int,input().split()))

Pow = S[P][Q]

Visited = [[False for _ in range(W)] for _ in range(H)]
Visited[P][Q] = True
# print(Visited)

def check_range(i, j):
    if 0 <= i and i <= H-1 and 0 <= j and j <= W-1:
        return True
    else:
        return False

Queue = []
heapq.heapify(Queue)

Vect = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for v in Vect:
    if check_range(P+v[0], Q+v[1]):
        if not Visited[P+v[0]][Q+v[1]]:
            Visited[P+v[0]][Q+v[1]] = True
            heapq.heappush(Queue, [ S[P+v[0]][Q+v[1]] , P+v[0], Q+v[1]])

# print(Queue)

check = True
while len(Queue) > 0 and check == True:
    Weak = heapq.heappop(Queue)
    i = Weak[1]
    j = Weak[2]
    if Weak[0] * X < Pow:
        Pow += Weak[0]
        for v in Vect:
            if check_range(i+v[0], j+v[1]):
                if not Visited[i+v[0]][j+v[1]]:
                    Visited[i+v[0]][j+v[1]] = True
                    heapq.heappush(Queue, [ S[i+v[0]][j+v[1]] , i+v[0], j+v[1] ])
    else:
        check = False

print(Pow)