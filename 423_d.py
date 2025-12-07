import heapq

N, K = map(int, input().split())

Ans = [0 for _ in range(N)]

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
C = [0 for _ in range(N)]
for i in range(N):
    A[i], B[i], C[i] = list(map(int, input().split()))

exit_data = []
heapq.heapify(exit_data)

space = K
i = 0
time = 0
while i < N:
    if C[i] <= space:
        if time < A[i]:
            time = A[i]
        Ans[i] = time
        heapq.heappush(exit_data, [time + B[i], C[i]])
        space -= C[i]
        i += 1
    else:
        exit_member = heapq.heappop(exit_data)
        if time < exit_member[0]:
            time = exit_member[0]
        space += exit_member[1]

for i in range(N):
    print(Ans[i])