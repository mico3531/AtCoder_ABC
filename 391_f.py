import heapq

N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

def make_num(i, j, k):
    return -1 * (A[i] * B[j] + B[j] * C[k] + C[k] * A[i])

def use(i, j, k):
    if i < N and j < N and k < N and (i, j, k) not in Used:
        Used.add((i, j, k))
        heapq.heappush(Queue, (make_num(i, j, k), i, j, k))

Queue = [(make_num(0, 0, 0), 0, 0, 0) ]
heapq.heapify(Queue)
Used = set((0,0,0))

for _ in range(K):
    tup = heapq.heappop(Queue)
    num, i, j, k = tup[0], tup[1], tup[2], tup[3]
    use(i+1, j, k)
    use(i, j+1, k)
    use(i, j, k+1)

print(-1 * num)