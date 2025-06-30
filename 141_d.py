import heapq

N, M = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    A[i] *= -1
heapq.heapify(A)

for j in range(M):
    x = heapq.heappop(A)
    x *= -1
    x //= 2
    x *= -1
    heapq.heappush(A, x)

ans = 0
for x in A:
    ans += x
ans *= -1
print(ans)